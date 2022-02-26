#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calulator!")
total_bill = input("What was the total bill? ")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#print(type(total_bill))
#print(type(tip_percentage))
#print(type(people))
#bill_and_tip = tip_percentage / 100 * total_bill + total_bill

bill_and_tip = int(tip_percentage) / 100 * float(total_bill) + float(total_bill) 
#price_per_person = bill_and_tip / int(people)
price_per_person = bill_and_tip / int(people)
result = "{:.2f}".format(price_per_person)
print(f"Each person will pay ${result}")