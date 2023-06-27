# Rock Paper Scissors
# Munteanu Mihnea @ Mihnea03

import random

def draw():
    print("Draw!")

def lose():
    print("You lost!")

def win():
    print("You won!")

def main():
    choices = ['Rock', 'Paper', 'Scissors']

    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    npc_choice = random.randint(0, 2)

    print(f"You chose: {choices[choice]}")
    print(f"The computer chose: {choices[npc_choice]}\n")

    if choice == 0:
        if npc_choice == 0:
            draw()
        elif npc_choice == 1:
            lose()
        else:
            win()
    elif choice == 1:
        if npc_choice == 0:
            win()
        elif npc_choice == 1:
            draw()
        else:
            lose()
    elif choice == 2:
        if npc_choice == 0:
            lose()
        elif npc_choice == 1:
            win()
        else:
            draw()
    else:
        print("Choice is invalid!")
    return

if __name__ == '__main__':
    main()