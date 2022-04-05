def clear():
  print("\n" * 50)

import random 
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# This function returns a random card from the deck
def deal():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#This function will calculate the score from 2 selected cards and check for blackjack
def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #check for ace if score is already over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def final_round(your_score, computer_score):
    if your_score > 21 and computer_score > 21:
        return "You Lose"
    if your_score == computer_score:
        return "Draw"
    elif your_score == 0:
        return "BlackJack! You Win"
    elif computer_score == 0:
        return "Computer wins Blackjack!"
    elif your_score > 21:
        "You went over. You Lose"
    elif computer_score > 21:
        return "Computer Loses"
    elif your_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play():
    print(logo)
    print("Welcome to BlackJack!")

    your_turn = []
    computer_turn = []
    game_over = False

    for _ in range(2):
        your_turn.append(deal())
        computer_turn.append(deal())

    while game_over == False:
    
        your_score = score(your_turn)
        computer_score = score(computer_turn)
        print(f"Your cards: {your_turn}, current score:{your_score}")
        print(f"computer's first card: {computer_turn[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            game_over = True

        else:
            choice = input("Type 'y' to get another card or type 'n' to pass ")
            if choice == "y":
                your_turn.append(deal())    
            if choice == "n":
                game_over = True
                

    while computer_score != 0 and computer_score < 17:
        computer_turn.append(deal())
        computer_score = score(computer_turn)

    print(f"Your final hand: {your_turn}, final score: {your_score}")
    print(f"Computer's final hand: {computer_turn}, final score: {computer_score}")
    print(final_round(your_score, computer_score))

option = input("Do you want to play a game of BlackJack? Type 'y' for yes or 'n' for no ")
if option == "y":
    play()
else:
    print("Goodbye")