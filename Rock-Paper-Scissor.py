import random

def display_instructions():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Type 'exit' to end the game.")

def get_user_choice():
    user_input = input("Enter your choice: ").strip().lower()
    if user_input == '1' or user_input == 'rock':
        return 'rock'
    elif user_input == '2' or user_input == 'paper':
        return 'paper'
    elif user_input == '3' or user_input == 'scissors':
        return 'scissors'
    elif user_input == 'exit':
        return None
    else:
        print("Invalid choice! Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        display_instructions()
        user_choice = get_user_choice()
        
        if user_choice is None:
            print("Thanks for playing!")
            break
        
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score: You - {user_score}, Computer - {computer_score}\n")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
