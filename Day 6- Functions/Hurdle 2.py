
print("Welcome to Reeborg's world")
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
    
while at_goal != True:
    hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
