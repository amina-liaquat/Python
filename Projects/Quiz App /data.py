"""
Data module for storing quiz questions and categories
"""

# Quiz questions database
QUESTIONS = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "correct": 2
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "correct": 1
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"],
            "correct": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "correct": 3
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1943", "1944", "1945", "1946"],
            "correct": 2
        }
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Go", "Gd", "Au", "Ag"],
            "correct": 2
        },
        {
            "question": "How many bones are in the human body?",
            "options": ["186", "206", "226", "246"],
            "correct": 1
        },
        {
            "question": "What is the speed of light?",
            "options": ["299,792 km/s", "199,792 km/s", "399,792 km/s", "499,792 km/s"],
            "correct": 0
        },
        {
            "question": "Which gas makes up most of Earth's atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "correct": 2
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Silver"],
            "correct": 2
        }
    ],
    "History": [
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "George Washington", "John Adams", "Benjamin Franklin"],
            "correct": 1
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1910", "1911", "1912", "1913"],
            "correct": 2
        },
        {
            "question": "Which ancient wonder of the world still stands today?",
            "options": ["Colossus of Rhodes", "Hanging Gardens", "Great Pyramid of Giza", "Lighthouse of Alexandria"],
            "correct": 2
        },
        {
            "question": "Who was the first person to walk on the moon?",
            "options": ["Buzz Aldrin", "Neil Armstrong", "John Glenn", "Yuri Gagarin"],
            "correct": 1
        },
        {
            "question": "Which empire was ruled by Julius Caesar?",
            "options": ["Greek Empire", "Roman Empire", "Persian Empire", "Egyptian Empire"],
            "correct": 1
        }
    ]
}

def get_categories():
    """Return list of available quiz categories"""
    return list(QUESTIONS.keys())

def get_questions(category):
    """Return questions for a specific category"""
    return QUESTIONS.get(category, [])
