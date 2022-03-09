import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
numb_of_letters = len(chosen_word)

for i in range(numb_of_letters):
  display.append('_')
print(display)

guess = input("Guess a letter: ").lower()
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display.remove('_')
        display.insert(position, guess)
print(display)