#global scope
from hashlib import new


enemies = 1

def increase_enemies():
    enemies = 2 #local scope
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Modifying Global Scope
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()


# There is no block scope in python

game_level = 3
enemies = ["Skeleton", "Zombie," "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
#If variable is created in a function, it is only availabe in that function



