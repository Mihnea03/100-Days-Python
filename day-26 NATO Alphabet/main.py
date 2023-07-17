# NATO Alphabet
# Munteanu Mihnea @ Mihnea03

import pandas as pd

DATA = 'data.csv'

def main():
    data = pd.read_csv(DATA)

    dictionary = {row.letter:row.code for (_, row) in data.iterrows()}
    
    word = input("Enter the word: ").upper()

    try:
        output = [dictionary[letter] for letter in word]
    except KeyError:
        output = "Sorry, only letters in the alphabet please."
    finally:
        print(output)
    return

if __name__ == '__main__':
    main()
