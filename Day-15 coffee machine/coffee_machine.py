from coffee_data import MENU
from coffee_data import resources

report = resources





# function that will calculate ingredients and subtracts from total resources

def coffee_flavor(choice):
    espresso = MENU["espresso"]["ingredients"]
    latte = MENU["latte"]["ingredients"]
    cappuccino = MENU["cappuccino"]["ingredients"]
    if choice == 'espresso':
        print(espresso)
    elif choice == 'latte':
        print(latte)
    elif choice == 'cappuccino':
        print(cappuccino)
    


choice = input("What would you like? 'espresso', 'latte', or 'cappuccino' ")
coffee_flavor(choice)