# COMMAND LINE APPLICATION: ROCK, PAPER, SCISSORS

# Author : Archit Tanwar
# Description:
# This application simulates the classic game "Rock, Paper, Scissors" where the user plays against the computer.
# The game will prompt the user to choose between "rock," "paper," or "scissors," and the computer will randomly select one as well.
# The game announces the winner after each round, keeps track of the score, and allows the user to play again if desired.

import random

# Function to get the user's choice
def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner based on user and computer choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the result of each round
def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

# Function to ask if the user wants to play again
def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again in ["yes", "no"]:
            return again == "yes"
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Main function to run the game loop
def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}\n")

        if not play_again():
            break

    print("\nThanks for playing!")

# Run the game
if __name__ == "__main__":
    main()
