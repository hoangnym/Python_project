### Using randomization and lists to play rock paper and scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]


def rock_paper_scissors():
    ## user_input
    valid_input = False

    while not valid_input:
        user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
        if user_input < 3 and user_input > -1:
            user_choice = choices[user_input]
            print(user_choice)
            valid_input = True
        else:
            print("Type a valid number between 0 and 2 inclusive.")

    print("Computer chose:")
    computer_choice = random.choice(choices)
    print(computer_choice)

    if user_choice == computer_choice:
        return "It is a draw"
    elif (user_choice == rock and computer_choice == paper) or (user_choice == paper and computer_choice == scissors) or (user_choice == scissors and computer_choice == rock):
        return f"You lose."
    else:
        return f"You win."


print(rock_paper_scissors())


