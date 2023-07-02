# Turtle Racing
# Munteanu Mihnea @ Mihnea03

from turtle import Turtle, Screen
from random import randint

def main():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    screen = Screen()

    screen.setup(width=500, height=400)
    color_guess = screen.textinput(title="Make your bet", prompt="Enter a color:")

    turtles = []

    index = 0
    
    for color in colors:
        new_turtle = Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(-screen.canvwidth / 2, -screen.canvheight / 2 + index * 60)
        new_turtle.pendown()
        turtles.append(new_turtle)
        index += 1
    
    winner = False
    while winner is False:
        for turtle in turtles:
            turtle.forward(randint(5, 10))
            if turtle.xcor() >= screen.canvwidth / 2:
                winner = True
                winning_color = turtle.color()[0]
                break
    
    if winning_color == color_guess:
        print("Congratulations! You guessed the correct color: {}".format(color_guess))
    else:
        print("Bad luck! {} won!".format(winning_color.capitalize()))
    return

if __name__ == '__main__':
    main()
