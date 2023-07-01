from question_model import Question
from data import question_data
import random

class Quiz:
    def __init__(self):
        self.quiz_list = []
        self.score = 0
        for question in question_data:
            q = Question(question["text"], question["answer"])
            self.quiz_list.append(q)

    def ask_question(self, nr):
        if len(self.quiz_list) == 0:
            print("No more questions remain! You won!")
            return False

        q = random.choice(self.quiz_list)
        self.quiz_list.remove(q)
        response = str(input(f"Q.{nr}: {q.text} (True/False)?: ")).capitalize()

        if response == q.answer:
            print(f"You got it right!\nThe correct answer was: {q.answer}")
            self.score += 1
            print(f"Your current score is: {self.score}/{nr}\n")
            return True
        else:
            print(f"That's wrong!\nThe correct answer was {q.answer}")
            print(f"Your current score is: {self.score}/{nr}\n")
            return False

