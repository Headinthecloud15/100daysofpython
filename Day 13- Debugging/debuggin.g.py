############DEBUGGING#####################

# # Describe Problem
def my_function():
    #range (1, 20) only includes numbers 1-19 so i never reaches 20. To debug change range to (1,21)
   for i in range(1, 20):
     if i == 20:
       print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) #indexerror happens at index 6 since dice_imgs list is 0 - 5.
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994: #year 1994 doesn't meet the condition since 1994 isn't < 1994 or > 1994
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# # Fix the Errors
age = input("How old are you?") #must turn the variable age to int
if age > 18:
    print("You can drive at age {age}.") #must use f string to combine str and int

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
# == evaluates if word_per_page is equal to the input. It will return False and give a 0 value to words_per_page
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item) #outside of for loop
    print(b_list) # Will only print [26] due to indent.

mutate([1,2,3,5,8,13])