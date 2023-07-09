# Name the States
# Munteanu Mihnea @ Mihnea03

import pandas
import turtle

IMAGE = "blank_states_img.gif"
DATA_FILE = "50_states.csv"

def main():
    screen = turtle.Screen()
    screen.title("Name the States")
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)

    data = pandas.read_csv(DATA_FILE)
    all_states = data["state"].to_list()
    guessed_states = []
    nr_guessed = 0

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{nr_guessed} / 50 Correct", prompt="What's another state's name?").capitalize()
        
        if answer_state in all_states:
            guessed_states.append(answer_state)
            nr_guessed += 1

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            
            state = data[data.state == answer_state]
            t.goto((int(state.x), int(state.y)))
            t.write(answer_state.capitalize(), align='center', font=("Arial", 6, 'normal'))
    
    turtle.mainloop()
    return

if __name__ == '__main__':
    main()
