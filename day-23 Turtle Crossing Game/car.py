from turtle import Turtle, colormode
import random

SPAWN_X = [310, 320]

class Car():
    def __init__(self, y):
        self.parts = []
        colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        for spawn in SPAWN_X:
            part = Turtle('square', visible=False)
            part.penup()
            part.pensize(10)
            part.setheading(180)
            part.color(r, g, b)
            part.goto(spawn, y)
            self.parts.append(part)
        
        for part in self.parts:
            part.showturtle()
    
    def move(self, distance):
        for part in self.parts:
            part.forward(distance)