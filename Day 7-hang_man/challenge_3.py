import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
numb_of_letters = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in range(numb_of_letters):
    display.append('_')

end = False  
while end == False:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display.remove('_')
        display.insert(position, guess)
  print(display)
  
  if '_' not in display:
    end = True
    print("You Win")