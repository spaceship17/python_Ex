# libraries import
import random

USER_WINS = 0  # constant declare
COMP_WINS = 0  # constant declare

options = ["rock", "paper", "Scissors"]  # variables declaration such as list,tuples, dictionary sets

while True:
    """takes user input and enters or exits the game."""
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in ["rock", "paper", "scissors"]:
        continue

    # to generate random numbers.
    # Rock :0, paper:1, Scissors: 2
    random_number = random.randint(0, 2)

    # assign the random integer to computer
    comp_pick = options[random_number]
    print("AutoBot Picked", comp_pick)

    # compare user input with comp pick / win conditions
    if user_input == 'rock' and comp_pick == 'scissor':
        print("you Won!")
        USER_WINS += 1
    elif user_input == 'paper' and comp_pick == 'rock':
        print("you Won!")
        USER_WINS += 1
    elif user_input == 'scissors' and comp_pick == 'paper':
        print("you Won!")
        USER_WINS += 1
    # Tie conditions
    elif user_input == 'scissors' and comp_pick == 'scissors':
        print("Tie!")
    elif user_input == 'rock' and comp_pick == 'rock':
        print("Tie!")
    elif user_input == 'paper' and comp_pick == 'paper':
        print("Tie!")
    else:
        print("you Lost!")
        COMP_WINS += 1

print("ConGrats ! You Won", USER_WINS, "times.")
print("Computer wins Won", COMP_WINS, "times.")

