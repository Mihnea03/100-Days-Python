# Pong
# Munteanu Mihnea @ Mihnea03

import time
from turtle import Turtle, Screen
from player import Player
from ball import Ball
from score_board import ScoreBoard

WIDTH = 800
HEIGHT = 600

P1_X = -370
P2_X = 370

PLAYER_1_UP = 'w'
PLAYER_1_DOWN = 's'

PLAYER_2_UP = 'Up'
PLAYER_2_DOWN = 'Down'

def main():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    screen.bgcolor('black')

    player1 = Player(P1_X)
    player2 = Player(P2_X)
    ball = Ball()
    scoreboard = ScoreBoard()

    def move_up_1():
        player1.move_up()
        pass

    def move_up_2():
        player2.move_up()
        pass

    def move_down_1():
        player1.move_down()
        pass

    def move_down_2():
        player2.move_down()
        pass

    screen.listen()
    screen.onkey(key=PLAYER_1_UP,fun=move_up_1)
    screen.onkey(key=PLAYER_2_UP,fun=move_up_2)
    screen.onkey(key=PLAYER_1_DOWN,fun=move_down_1)
    screen.onkey(key=PLAYER_2_DOWN,fun=move_down_2)

    while True:
        ball.move()
        if ball.verify_collision(player1, player2) is True:
            ball.home()
            ball.select_new_angle()
            time.sleep(0.5)
            scoreboard.update_scores(player1.score, player2.score)

        time.sleep(0.05)
        screen.update()

if __name__ == '__main__':
    main()
