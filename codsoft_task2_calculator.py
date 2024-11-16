# COMMAND LINE APPLICATION: CALCULATOR

# Author : Archit Tanwar
# Description:
# This command-line application allows you to perform basic arithmetic operations 
# including addition, subtraction, multiplication, division, modulus, floor division, and exponentiation.
# Proper exception handling is also included for division and modulus by zero.

def calculator():
    print("\n\n\t\t\tby @Archit Tanwar")
    print(" ")
    print("\n\t\t\t***CALCULATOR APPLICATION***\n")
    
    while True:
        print("\nAvailable Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Floor Division")
        print("7. Power")
        print("8. Exit")
        
        # Getting user input for operation choice
        try:
            choice = int(input("\nChoose an operation (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        # Exit case
        if choice == 8:
            print("\nExiting the Calculator...\n")
            break
        
        # Handling invalid input
        if choice not in range(1, 9):
            print("\nInvalid choice. Please select a valid option.")
            continue
        
        # Taking two numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        # Calling respective function based on user's choice
        if choice == 1:
            print(f"\nResult: {num1} + {num2} = {addition(num1, num2)}")
        elif choice == 2:
            print(f"\nResult: {num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == 3:
            print(f"\nResult: {num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == 4:
            division(num1, num2)
        elif choice == 5:
            modulus(num1, num2)
        elif choice == 6:
            floor_division(num1, num2)
        elif choice == 7:
            print(f"\nResult: {num1} ^ {num2} = {power(num1, num2)}")
        
        print("________________________________________")

# Function definitions for different operations

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("\nError: Division by zero is undefined.")
    else:
        print(f"\nResult: {a} / {b} = {a / b}")

def modulus(a, b):
    if b == 0:
        print("\nError: Modulus by zero is undefined.")
    else:
        print(f"\nResult: {a} % {b} = {a % b}")

def floor_division(a, b):
    if b == 0:
        print("\nError: Floor division by zero is undefined.")
    else:
        print(f"\nResult: {a} // {b} = {a // b}")

def power(a, b):
    return a ** b

# Main function to start the calculator
if __name__ == "__main__":
    calculator()
    print("\n\t\tThank you for using the Calculator!\n")
