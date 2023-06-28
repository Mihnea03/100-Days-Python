# PyPassword Generator
# Munteanu Mihnea @ Mihnea03

import string
import random

def main():
    print("Welcome to the PyPassword Generator!")
    
    letters = string.ascii_lowercase + string.ascii_uppercase
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password_list = []

    for i in range(0, nr_letters):
        password_list.append(random.choice(letters))
    
    for i in range(0, nr_symbols):
        password_list.append(random.choice(symbols))
    
    for i in range(0, nr_numbers):
        password_list.append(random.choice(string.digits))

    random.shuffle(password_list)
    password = ""

    for char in range(0, nr_letters + nr_numbers + nr_symbols):
        password += password_list[char]

    print(f"Your password is: {password}")

if __name__ == '__main__':
    main()