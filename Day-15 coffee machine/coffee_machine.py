from coffee_data import MENU
from coffee_data import resources


espresso = MENU["espresso"]["ingredients"]
latte = MENU["latte"]["ingredients"]
cappuccino = MENU["cappuccino"]["ingredients"]
espresso_price = 1.50
latte_price = 2.50
cappuccino_price = 3.00

# dictionary that stores the monetary value of the coins
money ={
    "quarter" : 0.25, 
    "dime" : 0.10,
   "nickel" : 0.05,
    "penny" : 0.01,
}


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

def money_inserted():
    quarters = int(input("How many quarters? ")) * money["quarter"]
    dimes = int(input("How many dimes? ")) * money["dime"]
    nickels = int(input("How many nickels? ")) * money["nickel"]
    pennies = int(input ("How many pennies? ")) * money ["penny"]
    total = "{:.2f}".format(quarters + dimes + nickels + pennies)
    print(total)

choice = input("What would you like? 'espresso', 'latte', or 'cappuccino' ")
if choice == 'report':
        print(resources)

total_price = "{:.2f}".format(total_amount(choice))
print(f"You're total is {total_price} Please insert coins ")
money_inserted()
#coffee_ingredients = coffee_flavor(choice)

# function that will take the input of coffee_ingredients and subtract it from the total resources

# function that will check if transaction is successful







# function that will check if resources are sufficient



