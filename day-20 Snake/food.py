from turtle import Turtle
import random

INTERVAL_MIN = -14
INTERVAL_MAX = 14

class Food:
    def __init__(self):
        x = 20 * random.randint(INTERVAL_MIN, INTERVAL_MAX)
        y = 20 * random.randint(INTERVAL_MIN, INTERVAL_MAX)
        self.x = x
        self.y = y
        food = Turtle()
        food.shape('circle')
        food.color('green')
        food.pensize(10)
        food.penup()
        food.goto(x, y)
        self.food = food
