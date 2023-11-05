import random

def play_game():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice in ["rock", "paper", "scissors"]:
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            result = "You win!"
        else:
            result = "Computer wins!"
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(f"Result: {result}")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

while True:
    play_game()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
