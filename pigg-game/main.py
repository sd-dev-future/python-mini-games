import random

# simulate rolling a six-sided die
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll

# ask the user for a valid number of players
while True:
    players=input("Enter number of players (2-4:): ")

    if players.isdigit():
        players=int(players)  # convert the string input into integer

        if 2<=players<=4:
            break
        else:
            print("Must be between 2-4 players ")
    else:
        print("Invalid, try again")


# The first player to pass this score wins !
max_score=50

# create list to score each player's total score
player_scores=[0 for _ in range(players)]

# continue until someone reaches the max
while max(player_scores)<max_score:

    # give each player a turn
    for i in range(players):
        print("\nplayer ",i+1," turn has just started.")
        print("Your total score is: ",player_scores[i],"\n")

        # Reset the score earned during the current turn
        current_score=0

        while True:

            should_roll=input("would you like to roll (y/n): ")

            # End the turn if the player chooses not to roll
            if should_roll.lower()!="y":
                break

            value=roll()

            # Rolling a 1 ends the turn and loses the turn's points
            if value==1:
                print("You rolled a 1! Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a: ",value)
            
            print("Your score is: ",current_score)

        player_scores[i] += current_score  
        print("Your total score is: ",player_scores[i])

# Find the player with the highest score
max_score=max(player_scores)
winning_index=player_scores.index(max_score)

print("\nplayer number ",winning_index+1," is the winner with a score of: ",max_score) 

