import os

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: Division by zero"

operations_dict = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    while True:
        number1 = float(input("Enter First Number: "))
        
        # Display available operations
        print("Available operations:")
        for symbol in operations_dict:
            print(symbol)

        continue_flag = True
        while continue_flag:
            op_symbol = input("Pick an Operation: ")

            # Check if the operation symbol is valid
            if op_symbol not in operations_dict:
                print("Warning: Invalid operation! Please choose a valid operation symbol (+, -, *, /).")
                continue  # Continue the loop and ask for a valid operation

            number2 = float(input("Enter Second Number: "))
            calculator_function = operations_dict[op_symbol]
            output = calculator_function(number1, number2)
            print(f"{number1} {op_symbol} {number2} = {output}")

            # Ask if the user wants to continue with the current result or start fresh
            should_continue = input(f"Enter \n ---> 'Y' to continue calculation with {output} \n ---> 'N' to start next calculation \n ---> 'x' to exit:").lower()
            if should_continue == 'y':
                number1 = output
            elif should_continue == 'n':
                continue_flag = False
                break
            elif should_continue == 'x':
                print("Bye! \n I hope i have solved your problem. \n Have a Nice Day")
                return  # Exit the program
            else:
                print("Invalid input! Exiting.")
                return  # Exit the program

if __name__ == "__main__":
    calculator()
