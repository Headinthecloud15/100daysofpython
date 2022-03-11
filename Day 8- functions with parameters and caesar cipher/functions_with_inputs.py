def greet():
    print("Hello")
    print("How are you?")
    print("Nice to meet you")

greet()

#function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"Nice to meet you {name}")

greet_with_name("Jenny")        #name is the parameter, Jenny is the argument

#functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")

greet_with("Jenny", "New York")

#functions with keyword arguments
greet_with(name="Jenny", location="New York")

    
