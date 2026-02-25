def print_menu():
    print("--- Menu ---")
    print("1. Print fruits in your home")
    print("2. Surprise me")
    print("0. Exit")
    print("------------\n")
    # It implicitly returns None
    #return None

    # Explicitly returns None
    return None


# return_value = print_menu()
# print(return_value)
# print(type(return_value))

# Parameters and Arguments
def add(x, y): # Parameters are indata, or input: x and y here are parameters
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x // y


def run_calculator():
    # Menu with while loop
    # - Print the menu
    # - Get user input
    # - Run operation based on input: add (+), subtract (-), multiply (*), divide (/)
    while True:
        result = None

        operation = input("Enter operation (+, -, *, /, or q to exit): ")
        if operation == "q":
            print("Terminating calculator... :/")
            break

        #if operation not in ["+", "-", "*", "/", "q"]:
        if operation not in "+-*/q":
            print("Invalid choice, try again.")
            continue

        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        if operation == "+":
            result = add(first_number, second_number) # when we provide input during when we call (invoke) a function, the values are called arguments
        elif operation == "-":
            result = subtract(first_number, second_number)
        elif operation == "*":
            result = multiply(first_number, second_number)
        elif operation == "/":
            result = divide(first_number, second_number)

        if result: # if True
            print(f"Result: {result}")
        # if result is None: # if it does not have a value
        #     pass
        # if result is not None: # if it has a value
        #     pass



run_calculator()