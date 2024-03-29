# OG script owner and credits goes to zaza102030
# GitHub: https://github.com/zaza102030
# Date uploaded (europe calendar): 2024/1/19, 00:07 AM
# Original script: https://gist.github.com/zaza102030/8950e8c84d50e590d7f057622b16f330

# Welcome to my Python quiz game! I created this project during my free time after a month of learning Python and programming in general. It's a simple yet pretty fun, it pulls questions from a special API (url is the API url = "https://opentdb.com/api.php").

# VERY IMPORTANT FOR SCRIPT TO WORK: Before you start, ensure you have the 'requests' library installed. If not, you can install it by running the following command in your terminal (cmd, PowerShell, etc.): pip install requests

# A crucial note: This script requires an internet connection to fetch questions from the API. If you're offline, you can always add your own questions and answers, though I kept it focused on on-line functionality. Feel free to modify the script as per your preferences.

# Here is the script, and have a nice day!

from numbers import Number
from numpy import integer, number
import requests
import random

print("OG script owner and credits goes to zaza102030")
print("# GitHub: https://github.com/zaza102030\n")
print("# Date uploaded: 2024/1/19, 00:07 AM")
print("# Original script: https://gist.github.com/zaza102030/8950e8c84d50e590d7f057622b16f330")

class QuizGame:
    def __init__(self):
        self.score = 0
        self.wins = 0
        self.loses = 0
        self.categories = {"General Knowledge": 9, "Science": 17, "History": 23}
        self.difficulties = ["easy", "medium", "hard"]

    def get_questions(self, category, difficulty, amount=5):
        url = "https://opentdb.com/api.php"
        params = {
            "amount": amount,
            "category": self.categories[category],
            "difficulty": difficulty,
            "type": "multiple",
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()["results"]
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch questions. Using default questions. Error: {e}")
            return []

    def ask_question(self, question, choices):
        print(question)
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

        user_answer = input("Enter the number of your answer: ")
        return int(user_answer)

    def run_quiz(self):
        print("Welcome to the Quiz Game!")

        category = random.choice(list(self.categories.keys()))
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        questions = self.get_questions(category, difficulty)

        if not questions:
            print("No questions available. Ending quiz.")
            return

        for question_num, question_data in enumerate(questions, 1):
            question = question_data["question"]
            choices = question_data["incorrect_answers"] + [question_data["correct_answer"]]
            correct_answer = len(choices)
            
            print(f"\nQuestion {question_num}:")
            user_answer = self.ask_question(question, choices)

            if user_answer == correct_answer:
                print("Correct!")
                self.score += 1
            else:
                self.loses += 1
                print(f"Wrong! The correct answer is {correct_answer}.")

        print(f"\nQuiz completed! Your score: {self.score}/{len(questions)}")
        if self.score == len(questions):
            self.wins += 1

    def reset_leaderboard(self):
        self.wins = 0
        self.loses = 0

def play():
    while True:
        quiz_game = QuizGame()
        quiz_game.run_quiz()

        print(f"\nLeaderboard: Wins = {quiz_game.wins}, Loses = {quiz_game.loses}")

        play_again = input('Would you like to play again (Y(es)/N(o))? ').lower()
        if play_again not in ['y', 'yes']:
            quiz_game.reset_leaderboard()
            print('Have a good day!')
            break

play()