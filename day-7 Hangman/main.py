# Hangman
# Munteanu Mihnea @ Mihnea03

import random
import time
import os

def file_read():
    with open('words.txt', 'r') as word_file:
        words = word_file.readlines()
    
    chosen_word = random.choice(words)
    chosen_word = chosen_word.replace('\n', '')

    return chosen_word

def main():
    chosen_word = file_read()

    print("Welcome to Hangman!\n")

    is_over = False
    lives = 6
    guessed_letters = []

    while is_over == False:
        os.system('clear')

        if lives == 0:
            is_over = True
            print(f"You lost!\nThe word was {chosen_word}")
            return
        
        ok = True
        for i in range(0, len(chosen_word)):
            if chosen_word[i] not in guessed_letters:
                ok = False
        
        if ok == True:
            print(f"You won!\nThe word was {chosen_word}")
            return

        for i in range(0, len(chosen_word)):
            if chosen_word[i] in guessed_letters:
                print(chosen_word[i], end="")
            else:
                print('_', end="")
        print("")
        
        print(f"Lives left: {lives}")
        


        guess = str(input("Guess a letter: "))
        print("")

        if guess in guessed_letters:
            print("You have already guessed this letter!\n")
            time.sleep(0.5)
        elif guess in chosen_word:
            guessed_letters.append(guess)
        else:
            lives -= 1
            print("This letter is not right!\n")
            guessed_letters.append(guess)
            time.sleep(0.5)
        
        

if __name__ == '__main__':
    main()