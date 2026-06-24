import random

# generate a random number
guess_num=random.randint(1,100)

while True:
    try:
        num=int(input("Enter a number between 1 and 100: "))
        if num>guess_num:
            print("Too high!")
        elif num<guess_num:
            print("Too low!")
        elif num==guess_num:
            print("You are correct")
            break
    # Exception handling
    except ValueError:
        print("Please enter a number")

    
    


   

