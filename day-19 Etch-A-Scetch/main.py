# Etch-A-Scetch
# Munteanu Mihnea @ Mihnea03

from turtle import Turtle, Screen

def main():
    pen = Turtle()
    screen = Screen()

    def move_forward():
        pen.forward(50)

    def move_backward():
        pen.backward(50)

    def rotate_left():
        pen.left(10)

    def rotate_right():
        pen.right(10)

    def quit_turtle():
        quit()

    def clear():
        pen.clear()
        pen.penup()
        pen.home()
        pen.pendown()

    screen.listen()
    screen.onkey(key="q", fun=quit_turtle)
    screen.onkey(key="c", fun=clear)
    screen.onkey(key="Up", fun=move_forward)
    screen.onkey(key="Down", fun=move_backward)
    screen.onkey(key="Left", fun=rotate_left)
    screen.onkey(key="Right", fun=rotate_right)

    screen.exitonclick()
    return

if __name__ == '__main__':
    main()
