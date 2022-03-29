#Add
from re import I


def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for i in operators:
    print (i)
operation_symbol = input("pick an operation from the line above:")

calculation_function = operators[operation_symbol]
answer = calculation_function(num1, num2)