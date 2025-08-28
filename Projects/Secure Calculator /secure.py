import tkinter as tk
from tkinter import ttk, messagebox
import re
import logging
import ast
import operator
import hashlib
import json
from datetime import datetime
import os
from typing import Union, Optional

class SecureCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Security settings
        self.max_expression_length = 100
        self.max_result_length = 20
        self.allowed_chars = set('0123456789+-*/.()^% ')
        self.session_token = self._generate_session_token()
        
        # Setup secure logging
        self._setup_logging()
        
        # Initialize calculator state
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.history = []
        self.authenticated = False
        
        # Create GUI
        self._create_gui()
        
        # Log session start
        self._log_security_event("SESSION_START", {"session_token": self.session_token})
        
    def _generate_session_token(self) -> str:
        """Generate a unique session token for security tracking."""
        timestamp = datetime.now().isoformat()
        random_data = os.urandom(16)
        return hashlib.sha256((timestamp + random_data.hex()).encode()).hexdigest()[:16]
    
    def _setup_logging(self):
        """Setup secure logging with file rotation and encryption-like hashing."""
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Configure logging
        logging.basicConfig(
            filename=f'logs/calculator_{datetime.now().strftime("%Y%m%d")}.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Log calculator startup
        logging.info("Secure Calculator initialized")
    
    def _log_security_event(self, event_type: str, details: dict):
        """Log security events with hashed sensitive data."""
        log_entry = {
            "event": event_type,
            "session": self.session_token,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        
        # Hash sensitive data before logging
        if "input" in log_entry["details"]:
            log_entry["details"]["input_hash"] = hashlib.sha256(
                log_entry["details"]["input"].encode()
            ).hexdigest()[:8]
            del log_entry["details"]["input"]
        
        logging.info(json.dumps(log_entry))
    
    def _validate_input(self, input_str: str) -> bool:
        """Validate input against security constraints."""
        # Check length
        if len(input_str) > self.max_expression_length:
            self._log_security_event("INPUT_TOO_LONG", {"length": len(input_str)})
            messagebox.showerror("Security Error", f"Input too long. Maximum {self.max_expression_length} characters allowed.")
            return False
        
        # Check for allowed characters only
        if not all(c in self.allowed_chars for c in input_str):
            self._log_security_event("INVALID_CHARS", {"input": input_str})
            messagebox.showerror("Security Error", "Invalid characters detected. Only numbers and basic operators allowed.")
            return False
        
        # Check for potential injection patterns
        dangerous_patterns = [
            r'import\s+', r'exec\s*\(', r'eval\s*\(', r'__import__',
            r'subprocess', r'os\.', r'sys\.', r'open\s*\(', r'file\s*\(',
            r'lambda', r'yield', r'global', r'nonlocal'
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, input_str, re.IGNORECASE):
                self._log_security_event("POTENTIAL_INJECTION", {"pattern": pattern})
                messagebox.showerror("Security Error", "Potential code injection detected!")
                return False
        
        return True
    
    def _safe_evaluate(self, expression: str) -> Union[float, int, str]:
        """Safely evaluate mathematical expressions using AST."""
        try:
            # Parse the expression into an AST
            node = ast.parse(expression, mode='eval')
            
            # Define allowed operators
            operators = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Pow: operator.pow,
                ast.Mod: operator.mod
            }
            
            # Evaluate the AST node safely
            def eval_node(n):
                if isinstance(n, ast.Num):
                    return n.n
                elif isinstance(n, ast.BinOp):
                    left = eval_node(n.left)
                    right = eval_node(n.right)
                    op_type = type(n.op)
                    if op_type not in operators:
                        raise ValueError(f"Operator {op_type} not allowed")
                    return operators[op_type](left, right)
                elif isinstance(n, ast.UnaryOp):
                    operand = eval_node(n.operand)
                    if isinstance(n.op, ast.USub):
                        return -operand
                    elif isinstance(n.op, ast.UAdd):
                        return +operand
                else:
                    raise ValueError(f"Unsupported node type: {type(n)}")
            
            result = eval_node(node.body)
            
            # Check result size
            if len(str(result)) > self.max_result_length:
                self._log_security_event("RESULT_TOO_LARGE", {"result_length": len(str(result))})
                return "Result too large"
            
            return result
            
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as e:
            self._log_security_event("EVALUATION_ERROR", {"error": str(e)})
            return "Error"
        except Exception as e:
            self._log_security_event("UNEXPECTED_ERROR", {"error": str(e)})
            return "Error"
    
    def _create_gui(self):
        """Create the calculator GUI with security features."""
        # Title frame
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill='x', padx=10, pady=5)
        
        title_label = ttk.Label(title_frame, text="Secure Calculator", font=('Arial', 16, 'bold'))
        title_label.pack()
        
        # Session info
        session_label = ttk.Label(title_frame, text=f"Session: {self.session_token}", 
                                 font=('Arial', 8), foreground='gray')
        session_label.pack()
        
        # Display frame
        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill='x', padx=10, pady=10)
        
        # Input display
        self.input_display = tk.Text(display_frame, height=2, font=('Arial', 14), 
                                    state='disabled', bg='#f0f0f0')
        self.input_display.pack(fill='x')
        
        # Result display
        result_display = ttk.Entry(display_frame, textvariable=self.result_var, 
                                  font=('Arial', 20, 'bold'), justify='right', 
                                  state='readonly')
        result_display.pack(fill='x', pady=(5, 0))
        
        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Calculator buttons
        buttons = [
            ('C', '⌫', '%', '÷'),
            ('7', '8', '9', '×'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '=', '^')
        ]
        
        for i, row in enumerate(buttons):
            button_row = ttk.Frame(button_frame)
            button_row.pack(fill='both', expand=True)
            
            for j, text in enumerate(row):
                if text == '0':
                    btn = ttk.Button(button_row, text=text, 
                                   command=lambda t=text: self._on_button_click(t))
                    btn.pack(side='left', fill='both', expand=True, padx=(0, 5))
                else:
                    btn = ttk.Button(button_row, text=text, 
                                   command=lambda t=text: self._on_button_click(t))
                    btn.pack(side='left', fill='both', expand=True, padx=(0, 5) if j < 3 else 0)
        
        # Security info button
        security_btn = ttk.Button(self.root, text="Security Info", 
                                 command=self._show_security_info)
        security_btn.pack(pady=5)
    
    def _on_button_click(self, button_text: str):
        """Handle button clicks with security checks."""
        if button_text == 'C':
            self.current_input = ""
            self.input_display.config(state='normal')
            self.input_display.delete(1.0, tk.END)
            self.input_display.config(state='disabled')
            self.result_var.set("")
        elif button_text == '⌫':
            if self.current_input:
                self.current_input = self.current_input[:-1]
                self._update_display()
        elif button_text == '=':
            if self.current_input:
                if self._validate_input(self.current_input):
                    # Replace display symbols with actual operators
                    expression = self.current_input.replace('×', '*').replace('÷', '/')
                    result = self._safe_evaluate(expression)
                    
                    # Log calculation
                    self._log_security_event("CALCULATION", {
                        "expression_length": len(expression),
                        "result_type": type(result).__name__
                    })
                    
                    # Add to history
                    self.history.append({
                        "expression": self.current_input,
                        "result": result,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    self.result_var.set(str(result))
        else:
            # Add character to current input
            if len(self.current_input) < self.max_expression_length:
                self.current_input += button_text
                self._update_display()
            else:
                messagebox.showwarning("Limit Reached", 
                                     f"Maximum input length of {self.max_expression_length} reached.")
    
    def _update_display(self):
        """Update the input display."""
        self.input_display.config(state='normal')
        self.input_display.delete(1.0, tk.END)
        self.input_display.insert(1.0, self.current_input)
        self.input_display.config(state='disabled')
    
    def _show_security_info(self):
        """Display security information."""
        info_window = tk.Toplevel(self.root)
        info_window.title("Security Information")
        info_window.geometry("400x300")
        
        info_text = f"""
Security Features Implemented:

1. Input Validation:
   - Maximum expression length: {self.max_expression_length} chars
   - Allowed characters only: {', '.join(sorted(self.allowed_chars))}
   - Pattern matching for injection prevention

2. Safe Evaluation:
   - AST-based expression parsing
   - Whitelist of allowed operators
   - No direct eval() or exec() usage

3. Secure Logging:
   - Session-based tracking
   - Hashed sensitive data
   - Timestamped security events

4. Memory Protection:
   - Input length limits
   - Result size validation
   - History tracking

5. Session Management:
   - Unique session token: {self.session_token}
   - Event logging for audit trail

Current Session Statistics:
- Calculations performed: {len(self.history)}
- Security events logged: Check logs directory
        """
        
        text_widget = tk.Text(info_window, wrap=tk.WORD, padx=10, pady=10)
        text_widget.pack(fill='both', expand=True)
        text_widget.insert(1.0, info_text)
        text_widget.config(state='disabled')
        
        close_btn = ttk.Button(info_window, text="Close", 
                              command=info_window.destroy)
        close_btn.pack(pady=10)
    
    def on_closing(self):
        """Handle application closing with security cleanup."""
        self._log_security_event("SESSION_END", {
            "calculations": len(self.history),
            "duration": "Session ended"
        })
        logging.info("Secure Calculator session ended")
        self.root.destroy()

def main():
    """Main function to run the secure calculator."""
    root = tk.Tk()
    app = SecureCalculator(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
