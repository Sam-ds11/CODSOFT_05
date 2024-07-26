import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the game result based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    
    return "You lose!"

def print_choices(user_choice, computer_choice):
    """Print the choices made by user and computer."""
    print(f"You chose: {user_choice.capitalize()}")
    print(f"The computer chose: {computer_choice.capitalize()}")

def main():
    """Main function to run the game loop and handle scoring."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        
        print_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
