# NATO Alphabet
# Munteanu Mihnea @ Mihnea03

import pandas as pd

DATA = 'data.csv'

def main():
    data = pd.read_csv(DATA)

    dictionary = {row[0]:row[1] for (_, row) in data.iterrows()}
    
    word = input("Enter the word: ").upper()

    output = [dictionary[letter] for letter in word]
    print(output)
    return

if __name__ == '__main__':
    main()
