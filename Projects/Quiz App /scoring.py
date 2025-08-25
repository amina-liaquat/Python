"""
Scoring module for handling quiz scores and statistics
"""

class ScoreManager:
    """Manages quiz scoring and statistics"""
    
    def __init__(self):
        self.current_score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.score_history = []
    
    def reset(self):
        """Reset current score"""
        self.current_score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
    
    def add_correct(self, points=10):
        """Add points for correct answer"""
        self.current_score += points
        self.correct_answers += 1
        self.total_questions += 1
    
    def add_wrong(self):
        """Record wrong answer"""
        self.wrong_answers += 1
        self.total_questions += 1
    
    def get_percentage(self):
        """Calculate percentage score"""
        if self.total_questions == 0:
            return 0
        return (self.correct_answers / self.total_questions) * 100
    
    def get_grade(self):
        """Get letter grade based on percentage"""
        percentage = self.get_percentage()
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"
    
    def save_score(self, category):
        """Save current score to history"""
        self.score_history.append({
            "category": category,
            "score": self.current_score,
            "percentage": self.get_percentage(),
            "grade": self.get_grade(),
            "correct": self.correct_answers,
            "total": self.total_questions
        })
    
    def get_summary(self):
        """Get score summary"""
        return {
            "score": self.current_score,
            "percentage": self.get_percentage(),
            "grade": self.get_grade(),
            "correct": self.correct_answers,
            "wrong": self.wrong_answers,
            "total": self.total_questions
        }
