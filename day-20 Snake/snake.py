from turtle import Turtle
from food import Food
from score import Score
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake = []

        for position in STARTING_POSITIONS:
            new_snake = Turtle()
            new_snake.shape('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(position)
            self.snake.append(new_snake)
        pass

    def move(self):
        for s_num in range(len(self.snake) - 1, 0, -1):
            self.snake[s_num].goto(self.snake[s_num - 1].position())
        
        self.snake[0].forward(MOVE_DISTANCE)
        pass

    def up(self):
        initial_angle = self.snake[0].heading()
        if initial_angle == 270:
            return
        self.snake[0].left(-initial_angle + 90)
        pass

    def down(self):
        initial_angle = self.snake[0].heading()
        if initial_angle == 90:
            return
        self.snake[0].left(-initial_angle - 90)
        pass

    def left(self):
        initial_angle = self.snake[0].heading()
        if initial_angle == 0:
            return
        self.snake[0].left(-initial_angle + 180)
        pass

    def right(self):
        initial_angle = self.snake[0].heading()
        if initial_angle == 180:
            return
        self.snake[0].left(-initial_angle)
        pass

    def create_new_snake(self):
        new_snake = Turtle()
        new_snake.shape('square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(self.snake[len(self.snake) - 1].position())
        self.snake.append(new_snake)

    def check_for_food(self, food:Food, score:Score):
        head = self.snake[0]
        (x, y) = head.position()
        (x_food, y_food) = food.food.position()

        if abs(x - x_food) < 10 and abs(y - y_food) < 10:
            food.food.setposition(500, 500)
            del food
            new_food = Food()
            self.create_new_snake()
            score.increase_score()
            return new_food
        else:
            return food
        
    def check_for_collision(self):
        head = self.snake[0]
        (x, y) = head.position()

        # Check for walls

        if x < -290 or y < -290:
            return True
        if x > 290 or y > 290:
            return True
        
        # Check for self collision

        for s_id in range(1, len(self.snake)):
            body_pos = self.snake[s_id].position()
            if body_pos == (x, y):
                return True
        
        return False