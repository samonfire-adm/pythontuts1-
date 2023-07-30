import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if opponent_choice == "scissors" else "Opponent wins!"
    elif user_choice == "paper":
        return "You win!" if opponent_choice == "rock" else "Opponent wins!"
    else:
        return "You win!" if opponent_choice == "paper" else "Opponent wins!"

def play_with_computer():
    user_wins = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win" in result:
            user_wins += 1
            print(f"Congratulations! You have won {user_wins} time(s).")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

def play_with_another_user():
    user1_wins = 0
    user2_wins = 0
    
    while True:
        user1_choice = get_user_choice()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        user2_choice = get_user_choice()
        print(f"User 1 chose: {user1_choice}")
        print(f"User 2 chose: {user2_choice}")
        result = determine_winner(user1_choice, user2_choice)
        print(result)
        
        if "You win" in result:
            user1_wins += 1
            print(f"User 1 wins {user1_wins} time(s).")
        elif "Opponent wins" in result:
            user2_wins += 1
            print(f"User 2 wins {user2_wins} time(s).")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Choose an option:")
    print("1. Play with Computer")
    print("2. Play with Another User")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        play_with_computer()
    elif choice == "2":
        play_with_another_user()
    else:
        print("Invalid choice. Please select 1 or 2.")
        main()

if __name__ == "__main__":
    main()
