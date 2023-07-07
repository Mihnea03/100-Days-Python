from car import Car
import random
import time

TRASH_COORDS = (1000, 1000)

MAX_Y = 220
MIN_Y = -220
DISTANCE = 20

class CarGenerator:
    def __init__(self, level):
        self.cars = []
        self.level = level

    def generate(self):
        for _ in range(random.randint(0, 1)):
            y = random.randint(MIN_Y, MAX_Y)
            new_car = Car(y)
            self.cars.append(new_car)

    def move_all(self):
        for car in self.cars:
            car.move(DISTANCE)

    def pause_level(self):
        time.sleep(1 / (self.level + 5))

    def clear_cars(self):
        for car in self.cars:
            for part in car.parts:
                part.goto(TRASH_COORDS)
                # del part
        self.cars = []
    
    def increase_level(self):
        self.level += 1
