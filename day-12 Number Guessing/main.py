# Number Guessing
# Munteanu Mihnea @ Mihnea03

import random

HARD_TURNS = 5
EASY_TURNS = 10

def choose_dificulty():
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

    if difficulty == 'easy':
        return EASY_TURNS
    elif difficulty == 'hard':
        return HARD_TURNS

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 101)
    attempts = choose_dificulty()

    while attempts != 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print("You have guessed the number! Good job!")
            return
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        
        attempts -= 1
    
    print("You have 0 attempts left... You lost!")
    return

if __name__ == '__main__':
    main()