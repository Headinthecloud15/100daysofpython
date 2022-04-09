EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ")
    if level == "easy":
        return EASY_ATTEMPTS
    if level == "hard":
         return HARD_ATTEMPTS


def answer(guess, number, attempts):
    if guess > number:
        print ("Too high. Guess again")
        return attempts - 1    
    elif guess < number:
        print("Too low. Guess again.")
        return attempts - 1
    elif guess == number:
        print("You guessed the magic number")
        

import random
from guessing_game_logo import logo

def game():
    print("Guess the magic number!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(0,100)

    print(f"the answer is {number}")
    attempts = difficulty()
    

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts left remaining")
        guess = int(input("Make a guess "))
        attempts = answer(guess, number, attempts)
        if attempts == 0:
            print("You have no more attempts. You lost")
            return

game()





    
