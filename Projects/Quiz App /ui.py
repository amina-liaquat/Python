"""
UI module for the quiz application interface
"""

import tkinter as tk
from tkinter import ttk, messagebox
from .quiz import Quiz

class QuizApp:
    """Main application class with GUI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        self.quiz = Quiz()
        self.current_question = None
        
        self.setup_styles()
        self.show_category_selection()
    
    def setup_styles(self):
        """Setup UI styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Title.TLabel', font=('Arial', 24, 'bold'), background='#f0f0f0')
        style.configure('Question.TLabel', font=('Arial', 16), background='#f0f0f0', wraplength=700)
        style.configure('Option.TButton', font=('Arial', 12), padding=10)
        style.configure('Progress.TLabel', font=('Arial', 12), background='#f0f0f0')
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_category_selection(self):
        """Show category selection screen"""
        self.clear_window()
        
        # Title
        title = ttk.Label(self.root, text="Quiz App", style='Title.TLabel')
        title.pack(pady=50)
        
        # Instructions
        instructions = ttk.Label(self.root, text="Select a category to start the quiz:", 
                               font=('Arial', 14), background='#f0f0f0')
        instructions.pack(pady=20)
        
        # Category buttons
        categories = self.quiz.score_manager.get_categories() if hasattr(self.quiz, 'score_manager') else []
        if not categories:
            from .data import get_categories
            categories = get_categories()
        
        for category in categories:
            btn = ttk.Button(self.root, text=category, 
                           command=lambda c=category: self.start_quiz(c),
                           style='Option.TButton')
            btn.pack(pady=10, padx=50, fill='x')
        
        # Exit button
        exit_btn = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_btn.pack(pady=30)
    
    def start_quiz(self, category):
        """Start quiz with selected category"""
        self.current_question = self.quiz.start_quiz(category)
        if self.current_question:
            self.show_question()
        else:
            messagebox.showerror("Error", "No questions available for this category")
            self.show_category_selection()
    
    def show_question(self):
        """Show current question"""
        self.clear_window()
        
        # Progress
        progress = self.quiz.get_progress()
        progress_label = ttk.Label(self.root, 
                                 text=f"Question {progress['current']} of {progress['total']}",
                                 style='Progress.TLabel')
        progress_label.pack(pady=10)
        
        # Progress bar
        progress_bar = ttk.Progressbar(self.root, length=700, mode='determinate')
        progress_bar['value'] = progress['percentage']
        progress_bar.pack(pady=5)
        
        # Question
        question_label = ttk.Label(self.root, text=self.current_question["question"],
                                 style='Question.TLabel')
        question_label.pack(pady=30, padx=50)
        
        # Options
        self.option_buttons = []
        for i, option in enumerate(self.current_question["options"]):
            btn = ttk.Button(self.root, text=option,
                           command=lambda idx=i: self.check_answer(idx),
                           style='Option.TButton')
            btn.pack(pady=5, padx=50, fill='x')
            self.option_buttons.append(btn)
        
        # Score display
        score_label = ttk.Label(self.root, 
                              text=f"Score: {self.quiz.score_manager.current_score}",
                              font=('Arial', 12), background='#f0f0f0')
        score_label.pack(pady=20)
    
    def check_answer(self, answer_index):
        """Check user's answer"""
        is_correct = self.quiz.submit_answer(answer_index)
        
        # Disable all buttons
        for btn in self.option_buttons:
            btn.state(['disabled'])
        
        # Show correct/wrong feedback
        if is_correct:
            messagebox.showinfo("Correct!", "Well done! That's the right answer.")
        else:
            correct_answer = self.current_question["options"][self.current_question["correct"]]
            messagebox.showinfo("Incorrect", f"Wrong answer. The correct answer is: {correct_answer}")
        
        # Check if quiz is complete
        if self.quiz.is_quiz_complete():
            self.show_results()
        else:
            self.current_question = self.quiz.get_next_question()
            self.show_question()
    
    def show_results(self):
        """Show quiz results"""
        self.clear_window()
        
        results = self.quiz.get_results()
        summary = results["summary"]
        
        # Title
        title = ttk.Label(self.root, text="Quiz Complete!", style='Title.TLabel')
        title.pack(pady=30)
        
        # Results frame
        results_frame = ttk.Frame(self.root)
        results_frame.pack(pady=20, padx=50, fill='both', expand=True)
        
        # Summary
        ttk.Label(results_frame, text=f"Category: {results['category']}", 
                 font=('Arial', 14)).pack(pady=5)
        ttk.Label(results_frame, text=f"Final Score: {summary['score']}", 
                 font=('Arial', 14)).pack(pady=5)
        ttk.Label(results_frame, text=f"Percentage: {summary['percentage']:.1f}%", 
                 font=('Arial', 14)).pack(pady=5)
        ttk.Label(results_frame, text=f"Grade: {summary['grade']}", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        ttk.Label(results_frame, text=f"Correct Answers: {summary['correct']}/{summary['total']}", 
                 font=('Arial', 14)).pack(pady=5)
        
        # Answer review
        review_frame = ttk.LabelFrame(results_frame, text="Answer Review", padding=10)
        review_frame.pack(pady=20, fill='both', expand=True)
        
        # Create scrollable frame for answers
        canvas = tk.Canvas(review_frame, height=200)
        scrollbar = ttk.Scrollbar(review_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add answers to scrollable frame
        for i, answer in enumerate(results["answers"]):
            status = "✓" if answer["is_correct"] else "✗"
            color = "green" if answer["is_correct"] else "red"
            
            answer_text = f"{i+1}. {status} {answer['question']}"
            label = ttk.Label(scrollable_frame, text=answer_text, font=('Arial', 10))
            label.pack(anchor='w', pady=2)
            
            if not answer["is_correct"]:
                correct_option = self.current_question["options"][answer["correct_answer"]]
                correct_text = f"   Correct answer: {correct_option}"
                ttk.Label(scrollable_frame, text=correct_text, 
                         font=('Arial', 9, 'italic')).pack(anchor='w', padx=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="New Quiz", 
                  command=self.show_category_selection).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Exit", 
                  command=self.root.quit).pack(side='left', padx=10)
