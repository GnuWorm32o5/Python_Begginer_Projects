import random

wins_against = {
    "rock": "scissors",
    "paper": "paper",
    "scissors": "paper",
}

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_input = str(input("Welcome to rock, paper, scisors - Please enter what you would like to choose with the exact string like rock paper or scissors:   "))
print(f"Computer has chosen {computer_choice}")

if user_input == computer_choice:
    print("It's a tie!")
elif wins_against[user_input] == computer_choice:
    print("You win!")
else:
    print("Computer wins!")

input("Press enter to leave the game")