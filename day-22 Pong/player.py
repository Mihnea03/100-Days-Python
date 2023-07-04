from turtle import Turtle

POSITIONS = [0, 20, 40, -20]
MOVE = 40

class Player:
    def __init__(self, x):
        self.score = 0
        self.parts = []
        for pos in POSITIONS:
            part = Turtle(shape='square')
            part.pensize(20)
            part.color('white')
            part.penup()
            part.goto((x, pos))
            self.parts.append(part)

    def move_up(self):
        for part in self.parts:
            part.setheading(90)
            part.forward(MOVE)

    def move_down(self):
        for part in self.parts:
            part.setheading(-90)
            part.forward(MOVE)
    
    def increase_score(self):
        self.score += 1