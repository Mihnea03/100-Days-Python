from turtle import Turtle
from player import Player
import random

MAX_LEFT = -380
MAX_RIGHT = 380
MAX_UP = 290
MAX_DOWN = -290

MOVE = 15

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.pensize(20)
        self.color('white')
        self.penup()

        self.select_new_angle()
        
    def select_new_angle(self):
        initial_angle = 0
        initial_angle = random.randint(-45, 45)

        if random.randint(0, 1) == 0:
            self.setheading(initial_angle)
        else:
            self.setheading(initial_angle + 180)

    def move(self):
        self.forward(MOVE)

    def change_angle_lr(self):
        self.setheading(180 - self.heading())
    
    def change_angle_ud(self):
        self.setheading(-self.heading())

    def verify_collision(self, player1:Player, player2:Player):
        (x, y) = self.position()

        for part in player1.parts:
            if part.distance(self) < 20:
                self.change_angle_lr()
                return False

        for part in player2.parts:
            if part.distance(self) < 20:
                self.change_angle_lr()
                return False

        if y >= MAX_UP or y <= MAX_DOWN:
            self.change_angle_ud()
        
        if x <= MAX_LEFT:
            player2.increase_score()
            return True
        
        if x >= MAX_RIGHT:
            player1.increase_score()
            return True
        
        return False

