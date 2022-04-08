import random
number = random.randint(0,100)
from guessing_game_logo import logo

print(f"the answer is {number}")

print("Guess the magic number!")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard'. ")

def easy_level():
    attempts = 10
    print("you have 10 attempts to guess the number")
    
