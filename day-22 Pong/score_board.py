from turtle import Turtle

POSITION = 240

class ScoreBoard:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0
        self.turtle = Turtle(visible=False)
        self.turtle.color('white')
        self.turtle.penup()
        self.turtle.goto(0, POSITION)
        self.turtle.write(f'{self.p1_score}   {self.p2_score}', align='center', font=("Calibri", 35, "bold"))

    def update_scores(self, score1, score2):
        self.p1_score = score1
        self.p2_score = score2

        self.turtle.clear()
        self.turtle.write(f'{self.p1_score}   {self.p2_score}', align='center', font=("Calibri", 35, "bold"))