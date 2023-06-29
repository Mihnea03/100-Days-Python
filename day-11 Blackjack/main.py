# Blackjack
# Munteanu Mihnea @ Mihnea03

import os
import random

def print_cards(player_cards, dealer_cards):
    print(f"Your cards: {player_cards}")
    print(f"Dealer's first card: {dealer_cards[0]}")

def add_card_to_player(player_cards, cards):
    player_cards.append(random.choice(cards))

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")) == 'y':
        os.system('clear')

        player_cards = random.choices(population=cards, k=2)
        dealer_cards = random.choices(population=cards, k=2)
        
        print_cards(player_cards, dealer_cards)

        while str(input("Type 'y' to get another card, type 'n' to pass: ")) != 'n':
            add_card_to_player(player_cards=player_cards, cards=cards)
            print_cards(player_cards, dealer_cards)
        
        print(f"Your final hand: {player_cards}")
        print(f"Dealer's final hand: {dealer_cards}")

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        if player_score == 0 and dealer_score != 0:
            print("Blackjack! You won!")
        elif dealer_score == 0 and player_score != 0:
            print("Blackjack! You lost!")
        else:
            if player_score > 21 and dealer_score <= 21:
                print("You lost!")
            elif dealer_score > 21 and player_score <= 21:
                print("You won!")
            else:
                if player_score == dealer_score:
                    max_player = max(player_cards)
                    max_dealer = max(dealer_cards)

                    if max_dealer > max_player:
                        print("You lost!")
                    elif max_dealer < max_player:
                        print("You won!")
                    else:
                        print("Draw!")
                elif player_score > dealer_score:
                    print("You won!")
                else:
                    print("You lost!")
    return

if __name__ == '__main__':
    main()