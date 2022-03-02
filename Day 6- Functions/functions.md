print("Hello") 
num_char = len("Hello")
print(num_char)

creating own function
def my_function():
    print("Hello")
    print("Bye")

to call a function
my_function()

Reeborg's world
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    
def jump():
    move()
    turn_right()
    turn_right()
    
def hurdle():
    move()
    turn_left()
    jump()
    turn_left()
    
for step in range(6):
    hurdle()