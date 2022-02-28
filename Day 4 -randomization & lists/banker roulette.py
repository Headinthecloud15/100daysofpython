import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

people = len(names)
pay = random.randint(0, people - 1)
print(f"{names[pay]} is going to buy the meal today!")