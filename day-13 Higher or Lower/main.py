# Higher or Lower
# Munteanu Mihnea @ Mihnea03

from data import data
import random
import os

def verify_if_win(A, B, choice):
    first = A['follower_count']
    second = B['follower_count']

    if choice == 'A' and first > second:
        return True
    
    if choice == 'B' and second > first:
        return True
    
    return False

def main():
    print("Welcome to Higher or Lower")

    score = 0
    comparing = random.choices(population=data, k=2)
    right = False

    while True:
        if right is True:
            print("You're right!", end=" ")
        print(f"Current score: {score}")

        A = comparing[0]
        B = comparing[1]
        print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
        print("VS")
        print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")

        choice = input("Type 'A' or 'B': ")

        if verify_if_win(A, B, choice) == True:
            right = True
            score += 1
        else:
            os.system('clear')
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        
        comparing[0] = comparing[1]
        comparing[1] = random.choice(data)
        os.system('clear')
 
if __name__ == '__main__':
    main()