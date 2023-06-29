# Secret Auction
# Munteanu Mihnea @ Mihnea03

import os

def main():
    print("Welcome to the secret auction program")

    more = True

    bidders = {}

    while more is True:
        name = str(input("What is your name? "))
        bid = int(input("What's your bid? "))

        next = str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))

        if next == 'no':
            more = False
        
        bidders[name] = bid
        os.system('clear')

    maximum_bid = 0
    maximum_name = ""

    for key in bidders.keys():
        if bidders[key] > maximum_bid:
            maximum_bid = bidders[key]
            maximum_name = key
    
    print(f"The auction winner is {maximum_name} with {maximum_bid}$!")

    return

if __name__ == '__main__':
    main()