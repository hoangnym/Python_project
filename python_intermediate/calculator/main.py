from art import logo

## Basic calculations

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide, 
}
def calculator():
    num1 = int(input("What is the first number?: "))
    next_iteration = True

    while next_iteration:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        ask_for_continuation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation.: ").lower()
        ### assign answer to new first variable
        if ask_for_continuation == 'y':
            num1 = answer
        elif ask_for_continuation == 'n':
            next_iteration = False
            calculator()
        else:
            print("This is no valid answer.")
            break

calculator()
