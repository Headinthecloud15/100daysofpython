# Variable data is a list of dictionaries.
# key:value pair being compared is follower_count
import random 
from game_data import data


#print(random.choice(list(data)))
# print random dictionary from list data
item_a = random.choice(data)
print(item_a["name"])
print(item_a["description"])
print(item_a["country"])

print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}") 




