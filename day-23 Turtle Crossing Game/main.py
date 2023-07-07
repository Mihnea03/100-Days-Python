# Turtle Crossing Game
# Munteanu Mihnea @ Mihnea03

from turtle import Screen
from car_generator import CarGenerator
from player import Player, MOVE
import time

WIDTH = 600
HEIGHT = 600

UP_KEY = 'Up'
DOWN_KEY = 'Down'

def main():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    
    game_is_on = True
    level = 1
    cargen = CarGenerator(level)
    player = Player()

    def move_up():
        player.forward(MOVE)
    
    def move_down():
        player.backward(MOVE)

    screen.listen()
    screen.onkey(key=UP_KEY, fun=move_up)
    screen.onkey(key=DOWN_KEY, fun=move_down)

    while game_is_on:
        if player.check_victory():
            cargen.clear_cars()
            level += 1
            cargen.increase_level()
            player.reset()
            time.sleep(0.5)
        
        if player.check_collision(cargen):
            time.sleep(1)
            return

        cargen.generate()
        cargen.move_all()
        cargen.pause_level()


        screen.update()
    return

if __name__ == '__main__':
    main()
