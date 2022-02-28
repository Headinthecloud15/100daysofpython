rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choose = [rock, paper, scissors]
your_choice = int(input("rock, paper, scissors? Choose 0 for rock, 1 for paper or 2 for scissors "))
print(choose[your_choice])

import random
computer_choice = random.randint(0,2)
print(f"computer chose {choose[computer_choice]}")

if your_choice == 0:
  if computer_choice == 0:
    print("This game is a draw!")
  elif computer_choice == 1:
    print("computer wins!")
  elif computer_choice == 2:
    print("You win!")
if your_choice == 1:
  if computer_choice == 0:
    print("You win!")
  elif computer_choice == 1:
    print("This game is a draw!")
  elif computer_choice == 2:
    print("computer wins!")
if your_choice == 2:
  if computer_choice == 0:
    print("computer wins!")
  elif computer_choice == 1:
    print("You win!")
  elif computer_choice == 2:
    print("This game is a draw")
