import random 
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")

if choice == "y":
    print(logo)
    print("Welcome to BlackJack!")
    your_turn = random.choices(cards, k=2)
    your_score = sum(your_turn)
    computer_turn = random.choices(cards, k=2)
    computer_score =sum(computer_turn)
    print(f"your cards: {your_turn}, current score: {your_score}")
    print(f"Computer's first card: {computer_turn[0]}")
    choice_2 = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice_2 == "y":
        final_hand = your_score + int(random.choice(cards))
        print(final_hand)
else:
    print("Goodbye")





ace = cards[0]
ace2 = cards[1]
jack = cards[10]
queen = cards[11]
king = cards[12]