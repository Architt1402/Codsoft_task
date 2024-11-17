# COMMAND LINE APPLICATION: RANDOM PASSWORD GENERATOR

# Author : Archit Tanwar
# Description:
# This application generates a random password based on the user's input for the desired length.
# It allows users to either accept the generated password, regenerate a new one, or exit the application.

import random
import string

def password_generator():
    print("\n\n\t\t\tby @Archit Tanwar")
    print("________________________________________")
    print("\n\t\t\t*** RANDOM PASSWORD GENERATOR ***\n")
    
    # Getting username from the user
    username = input("\tEnter your username: ")
    
    # Getting desired password length from the user
    while True:
        length = input("\n\tEnter the desired password length: ")
        if length.isdigit() and int(length) > 0:
            password = generate_password(int(length))
            break
        else:
            print("\n\tInvalid length. Please enter a positive integer.")

    # Main loop to allow password regeneration or acceptance
    while True:
        print(f"\n\tGenerated password for {username}: {password}\n")
        choice = menu_options()

        if choice == "1":
            print("\n\tPassword accepted!")
            break
        elif choice == "2":
            password = generate_password(int(length))
        elif choice == "3":
            print("\n\tThank you for using the Random Password Generator!")
            break
        else:
            print("\n\tInvalid choice. Please select a valid option.")

    print("\n\tGoodbye! Thank you for using the app.\n")

# Function to generate a random password of given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to display the menu and return user's choice
def menu_options():
    print("""\n\t1. Accept the password
    \t2. Regenerate a new password
    \t3. Exit""")
    return input("\n\tEnter your choice: ")

# Main function
if __name__ == "__main__":
    password_generator()
