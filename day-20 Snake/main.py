# Snake
# Munteanu Mihnea @ Mihnea03

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    game_is_on = True


    while game_is_on:
        screen.update()
        time.sleep(0.1)

        if snake.check_for_collision():
            game_is_on = False

        food = snake.check_for_food(food, score)   
        snake.move()

    screen.exitonclick()
    return

if __name__ == '__main__':
    main()
