import random
number = random.randint(0,100)
from guessing_game_logo import logo

print(f"the answer is {number}")

print("Guess the magic number!")
print("I'm thinking of a number between 1 and 100")

#level = input("Choose a difficulty. Type 'easy' or 'hard'. ")

# easy
end = False
while end == False:
    attempts = 10
    guess = int(input("Make a guess "))

    while guess > number or guess < number:
        attempts -= 1
        if attempts == 0:
            end = True
            print("You Lose")
        print (f"You have {attempts} attempts remaining to guess the number")




