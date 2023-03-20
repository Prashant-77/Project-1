''' This code is written by me
Author= Prashant Prakash '''

import random

while True:
    # get user input
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    
    # validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter either Rock, Paper, or Scissors.")
        continue
    
    # get computer's random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose", computer_choice)
    
    # determine the winner
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
    
    # ask user to play again
    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again != "yes":
        break
