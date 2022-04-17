from coffee_data import MENU
from coffee_data import resources


espresso = MENU["espresso"]["ingredients"]
latte = MENU["latte"]["ingredients"]
cappuccino = MENU["cappuccino"]["ingredients"]
espresso_price = 1.50
latte_price = 2.50
cappuccino_price = 3.00

def coffee_flavor(choice):
    """function that will take input and return ingredients"""
    if choice == 'espresso':
        return espresso
    elif choice == 'latte':
        return latte
    elif choice == 'cappuccino':
        return cappuccino
    
    
#  calculate total amount to pay
def total_amount(choice):
    if choice == 'espresso':
       return espresso_price
    elif choice == 'latte':
        return espresso_price
    elif choice == 'cappuccino':
        return espresso_price



choice = input("What would you like? 'espresso', 'latte', or 'cappuccino' ")
if choice == 'report':
        print(resources)


print(f"You're total is {total_amount(choice)} Please insert coins ")

coffee_ingredients = coffee_flavor(choice)

# function that will take the input of coffee_ingredients and subtract it from the total resources

# function that will check if transaction is successful

quarters = input("How many quarters? ")



# Calculate the monetary value of the coins
quarter = 0.25 * int(quarters)
dime = 0.10
nickel = 0.05
penny = 0.01
total = quarter 
print (total)
# function that will check if resources are sufficient



