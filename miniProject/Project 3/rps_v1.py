import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    else:
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()
