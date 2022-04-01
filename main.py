#   rock paper scissors is a game for 2 or more players
#   participants get to say "rock paper scissors" and then simultaneously form their hands into the shape of
#   a rock(fist), a piece of paper(palm facing downwards) or a pair of scissors(2 fingers extended)
#   The rules here are pretty straightforward:

#   rock smashes scissors
#   paper covers rock
#   scissors cut paper

#   How the game works
#   Take a user input(rock, paper, scissors)
#   Make the computer choose
#   determine the winner

import random

user_turn = input("Enter a choice (rock, paper, scissors): ")
possible_actions= ["rock","paper","scissors"]
computer_turn= random.choice(possible_actions)
print(f"\n Your choice was {user_turn}, and computer chose {computer_turn}.\n")

if user_turn == computer_turn:
   print(f"Both players selected {user_turn}, it's a tie")
elif user_turn == "rock":
    if computer_turn == "scissors":
        print("rock smashes scissors, you win!")
    else:
        print("paper covers rock, you lose")
elif user_turn == "paper":
    if computer_turn == "rock":
        print("paper covers rock,you win!")
    else:
        print("scissors cuts paper, you win!")
elif user_turn == "scissors":
    if computer_turn == "paper":
        print("scissors cuts paper, you win!")
    else:
        print("rock smashes scissors, you lose")

