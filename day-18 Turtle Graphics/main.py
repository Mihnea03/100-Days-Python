# Turtle Graphics
# Munteanu Mihnea @ Mihnea03

from turtle import Turtle, Screen, colormode
from random import choice, randint
import colorgram

PICTURE = 'spots.jpg'

def main():
    turtle = Turtle()
    turtle.shape('turtle')
    colormode(255)

    # This was used to extract the colors from a Damien Hirst painting

    # rgb_values = []
    # colors = colorgram.extract(PICTURE, 30)
    # for color in colors:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b = color.rgb.b
    #     rgb_values.append((r, g, b))

    colors = [(253, 251, 247), (253, 247, 250), (236, 252, 244), (249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]

    turtle.penup()
    turtle.setposition(-250, -200)

    for i in range(0, 10):
        curr_pos = turtle.position()

        for j in range(0, 10):
            turtle.pendown()
            turtle.dot(20, choice(colors))
            turtle.penup()

            turtle.forward(50)
        
        turtle.setposition((curr_pos[0], curr_pos[1] + 50))

    screen = Screen()
    screen.exitonclick()
    return

if __name__ == '__main__':
    main()
