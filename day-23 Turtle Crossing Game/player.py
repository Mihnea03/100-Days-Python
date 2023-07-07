from turtle import Turtle
from car_generator import CarGenerator

START_POS = (0, -270)
MOVE = 30
VICTORY_Y = 270

class Player(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.pensize(15)
        self.penup()
        self.goto(START_POS)
        self.setheading(90)

    def check_victory(self):
        if self.position()[1] >= VICTORY_Y:
            return True
        return False
    
    def reset(self):
        self.goto(START_POS)
        self.setheading(90)
    
    def check_collision(self, cargen:CarGenerator):
        for car in cargen.cars:
            for part in car.parts:
                if self.distance(part) <= 5:
                    return True
        return False