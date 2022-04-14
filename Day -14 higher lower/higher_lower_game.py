# Variable data is a list of dictionaries.
# key:value pair being compared is follower_count
def clear():
  print("\n" * 50)


import random 
from game_data import data
from game_art import logo
from game_art import vs 


# function that returns random account from data list
def random_account():
    return random.choice(data)

# function that returns data from random account and formats it
def account_format(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f" {name}, a {description}, from {country}"

#function that checks user's guess
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random_account()
  account_b = random_account()

  while game_should_continue:
    account_a = account_b
    account_b = random_account()

    while account_a == account_b:
      account_b = random_account()

    print(f"Compare A: {account_format(account_a)}.")
    print(vs)
    print(f"Against B: {account_format(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()


