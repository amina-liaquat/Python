"""
Quiz module for managing quiz logic and flow
"""

from .data import get_categories, get_questions
from .scoring import ScoreManager

class Quiz:
    """Main quiz class that manages quiz flow"""
    
    def __init__(self):
        self.score_manager = ScoreManager()
        self.current_category = None
        self.current_question_index = 0
        self.questions = []
        self.current_question = None
        self.user_answers = []
    
    def start_quiz(self, category):
        """Start a new quiz with selected category"""
        self.current_category = category
        self.questions = get_questions(category)
        self.current_question_index = 0
        self.user_answers = []
        self.score_manager.reset()
        return self.get_next_question()
    
    def get_next_question(self):
        """Get the next question in the quiz"""
        if self.current_question_index < len(self.questions):
            self.current_question = self.questions[self.current_question_index]
            return self.current_question
        return None
    
    def submit_answer(self, answer_index):
        """Submit an answer and update score"""
        if self.current_question is None:
            return False
        
        correct = answer_index == self.current_question["correct"]
        self.user_answers.append({
            "question": self.current_question["question"],
            "user_answer": answer_index,
            "correct_answer": self.current_question["correct"],
            "is_correct": correct
        })
        
        if correct:
            self.score_manager.add_correct()
        else:
            self.score_manager.add_wrong()
        
        self.current_question_index += 1
        return correct
    
    def is_quiz_complete(self):
        """Check if quiz is complete"""
        return self.current_question_index >= len(self.questions)
    
    def get_results(self):
        """Get quiz results"""
        self.score_manager.save_score(self.current_category)
        return {
            "summary": self.score_manager.get_summary(),
            "answers": self.user_answers,
            "category": self.current_category
        }
    
    def get_progress(self):
        """Get current quiz progress"""
        return {
            "current": self.current_question_index + 1,
            "total": len(self.questions),
            "percentage": ((self.current_question_index + 1) / len(self.questions)) * 100 if self.questions else 0
        }
