import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to get player's choice
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice! Please try again.")

# Function to get computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


# Main game loop
while True:
    # Get player and computer choices
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    # Determine the winner
    winner = determine_winner(player_choice, computer_choice)

    # Display the choices and result
    print(f"\nYour choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"\n{winner}\n")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
