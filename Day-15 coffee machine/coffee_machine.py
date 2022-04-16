from coffee_data import MENU
from coffee_data import resources

report = resources
espresso = MENU["espresso"]["ingredients"]
latte = MENU["latte"]["ingredients"]
cappuccino = MENU["cappuccino"]["ingredients"]

# function that will take input and return ingredients

def coffee_flavor(choice):
    if choice == 'espresso':
        return espresso
    elif choice == 'latte':
        return latte
    elif choice == 'cappuccino':
        return cappuccino
    

choice = input("What would you like? 'espresso', 'latte', or 'cappuccino' ")
coffee_ingredients = coffee_flavor(choice)
print(resources - coffee_ingredients)

