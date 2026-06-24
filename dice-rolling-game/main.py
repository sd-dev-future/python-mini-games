import random

count=0

while True:
    # get user input and convert to lower case
    choice=input("Roll the dice? (y/n): ").lower()

    if choice=="y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)

        print(f'({die1},{die2})')
        # To get how many times the dice was rolled
        count=count+1

    elif choice=="n":
        print("Thank you!")
        break
    else:
        print("Invalid number")
    
    
# Print count
print(f'("The dice was rolled {count} times throughout the game.")')

    
