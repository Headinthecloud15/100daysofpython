# Variable data is a list of dictionaries.
# key:value pair being compared is follower_count
import random 
from game_data import data
from game_art import logo
from game_art import vs 


# assign random dictionary from data list to variable
item_a = random.choice(data)
item_b = random.choice(data)
if item_a == item_b:
    item_b = random.choice(data)

print (logo)



game_end = False
while game_end == False:
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}") 

    print(vs) 
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}") 

    final_score = 0
    choice = input("Who has more followers? Type 'A' or 'B':").lower() 

    a_followers = item_a['follower_count']
    b_followers = item_b['follower_count']

    
# checks users choice and prints if they are right or wrong
    if a_followers > b_followers:
        if choice == "a":
            final_score += 1
            print(f"You're right. Current score {final_score}")
        else:
            end = True
            print(f"Sorry that's wrong. Final score {final_score}")
    elif b_followers > a_followers:
        if choice == "b":
            final_score += 1
            print(f"You're right. Current score {final_score}")
        else:
            end = True
            print(f"Sorry that's wrong. final score {final_score}")







