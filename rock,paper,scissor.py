Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## ROCK PAPER AND SCISSORS GAME
... 
... import random
... def get_user_choice():
...     user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
...     while user_choice not in ["rock", "paper", "scissors"]:
...         print("Invalid choice. Please choose Rock, Paper, or Scissors.")
...         user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
...     return user_choice
... def get_computer_choice():
...     return random.choice(["rock", "paper", "scissors"])
... def determine_winner(user, computer):
...     if user == computer:
...         return "It's a tie!"
...     elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
...         return "You win!"
...     else:
...         return "Computer wins!"
... def play_game():
...     print("Let's play Rock, Paper, Scissors!")
...     user_choice = get_user_choice()
...     computer_choice = get_computer_choice()
...     print(f"You chose {user_choice}. Computer chose {computer_choice}.")
...     print(determine_winner(user_choice, computer_choice))
... # Play the game
