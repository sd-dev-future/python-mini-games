import random

ROCK='r'
PAPER='p'
SCISSORS='s'
icons={ROCK:'🪨',PAPER:'📄',SCISSORS:'✂️'}
choices=tuple(icons.keys())  # icons.keys() are -> ROCK,PAPER,SCISSORS  & Tuple used so cannot change the values


def get_user_choice():
    while True:

        user_choice=input("Enter rock, paper or scissors (r/p/s): ").lower()

        if user_choice in choices:
            return user_choice
        else:
            print("Invalid input.")
            continue


def display_choices(user_choice,computer_choice):
    print(f'Your choise is {icons[user_choice]}')
    print(f'Computer\'s choice is {icons[computer_choice]}')


def select_winner(user_choice,computer_choice):
    if (user_choice==computer_choice):
        print("Tie !")
    elif(
        (user_choice==ROCK and computer_choice==SCISSORS) or 
        (user_choice==SCISSORS and computer_choice==PAPER) or 
        (user_choice==PAPER and computer_choice==ROCK)):
        print("You won !")
    else:
        print("You lose !")


def play_game():
    while True:
        user_choice=get_user_choice()
        computer_choice=random.choice(choices)

        display_choices(user_choice,computer_choice)

        select_winner(user_choice,computer_choice)

        should_continue=input("Do you want to continue (y/n): ").lower()

        if should_continue=='n':
            break
        
play_game()







    

    

    
