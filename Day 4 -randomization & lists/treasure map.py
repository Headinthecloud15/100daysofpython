row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if int(position) == 11:
    map[0][0] = "X"
elif int(position) == 12:
    map[1][0] = "X"
elif int(position) == 13:
    map[2][0] = "X"
elif int(position) == 21:
    map[0][1] = "X"
elif int(position) == 22:
    map[1][1] = "X"
elif int(position) == 23:
    map[2][1] = "X"
elif int(position) == 31:
    map[0][2] = "X"
elif int(position) == 32:
    map[1][2] = "X"
elif int(position) == 33:
    map[2][2] =="X"
else:
    print("Invalid")

print(f"{row1}\n{row2}\n{row3}")