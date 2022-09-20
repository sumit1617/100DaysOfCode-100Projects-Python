import calc_logo


# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(calc_logo.logo)
    num1 = float(input("What's the first number?: "))
    for symbols in operations:
        print(symbols)
    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)
        print(answer)

        if input(f"Type 's' to continue calculating with {answer}, or type 'n' to start with new calculation: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()