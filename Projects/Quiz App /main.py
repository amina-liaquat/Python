"""
Main entry point for the Quiz App
"""

import tkinter as tk
from .ui import QuizApp

def main():
    """Main function to run the quiz application"""
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
