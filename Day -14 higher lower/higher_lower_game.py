# Variable data is a list of dictionaries.
# key:value pair being compared is follower_count
import random 
from game_data import data
from game_art import logo
from game_art import vs 

#print(random.choice(list(data)))
# assign random dictionary from data list to variable
item_a = random.choice(data)
item_b = random.choice(data)
if item_a == item_b:
    item_b = random.choice(data)





final_score = []
print (logo)

print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}") 

print(vs) 
print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}") 

choice = input("Who has more followers? Type 'A' or 'B':").lower() 

a_followers = item_a['follower_count']
b_followers = item_b['follower_count']

if a_followers > b_followers:
    if choice == "a":
        print("You're right")
    else:
        print("Sorry that's wrong")
elif b_followers > a_followers:
    if choice == "b":
        print("You're right")
    else:
        print("Sorry that's wrong")


#highest = max(A,B)
#print(highest)

#if choice >= highest:
    #print("You're right")
#else:
    #print("Sorry that's wrong")




