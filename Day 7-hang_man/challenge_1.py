import random

word_list = ["ardvark", "baboon", "camel"]

#randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

#ask the user to guess a letter and assign answer to variable called guess. Make guess lowercase.
guess = input("Guess a letter ").lower()

#check if the letter guessed is one of the letters in the chosen_word

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Incorrect")
        