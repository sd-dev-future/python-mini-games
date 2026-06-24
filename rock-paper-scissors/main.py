import random

choices=['r','p','s']

icons={'r':'🪨','p':'📄','s':'✂️'}

while True:
    user_choice=input("Enter rock, paper or scissors (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invali choice!")
        continue

    computer_choice=random.choice(choices)


    print(f'Your choise is {icons[user_choice]}')
    print(f'Computer\'s choice is {icons[computer_choice]}')

    if (user_choice==computer_choice):
        print("Tie !")
    elif(
        (user_choice=='r' and computer_choice=='s') or 
        (user_choice=='s' and computer_choice=='p') or 
        (user_choice=='p' and computer_choice=='r')):
        print("You won !")
    else:
        print("You lose !")

    should_continue=input("Do you want to continue (y/n): ").lower()

    if should_continue=='n':
        break
