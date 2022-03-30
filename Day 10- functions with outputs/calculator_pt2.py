def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for i in operators:
    print (i)

not_end = True

while not_end == True:
    operation_symbol = input("pick an operation ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operators[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if choice == "y":
        num1 = answer
    else:
        not_end == False
