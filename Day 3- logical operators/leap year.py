year = int(input("Which year do you want to check? "))

#Leap = year % 4 == 0
#Not_Leap = year % 100 == 0
#Leap2 = year % 400 == 0

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else: 
    print("Not Leap year")
