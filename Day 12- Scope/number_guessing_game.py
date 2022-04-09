def hard_level():
    attempts = 5

def game():
    end = False
    while end == False:
        
        guess = int(input("Make a guess "))
        if guess > number:
            print ("Too high. Guess again")    
        elif guess < number:
            print("Too low. Guess again.")
        elif guess == number:
            print("You guessed the magic number")
        

import random
from guessing_game_logo import logo

number = random.randint(0,100)

print(f"the answer is {number}")
attempts = 10

print("Guess the magic number!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard'. ")

if level == "easy":
    game()
if level == "hard":
    hard_level()
    game()
