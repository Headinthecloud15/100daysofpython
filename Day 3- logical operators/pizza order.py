print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

#Small = 15
#Medium = 20
#Large = 25
#pepperoni_for_small = 2
#pepperoni_for_medium_or_large = 3
#extra_cheese_any = 1

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L": 
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
        
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is {bill}")