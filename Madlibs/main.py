print("Choose a story you like little sunshine 🌻: ")

print("1️⃣ - The Magical Unicorn 🦄")
print("2️⃣ - The Dinosaur's Birthday Party 🦕")
print("3️⃣ - The lost Space Puppy 🐶")

story_numbers=tuple([1,2,3])

    
def chooseStory():
    while True:
        try:
            storyNumber=int(input("Enter 1 or 2 or 3 : "))
            if storyNumber not in story_numbers:
                print("Invalid story number. Please enter 1, 2, 3 🌻")
                continue
            return storyNumber
        except ValueError:
            print("Please enter a number only ! 😊")



def Magical_Unicorn():
    
    adjective=input("Enter an adjective : ")
    colour=input("Enter a colour : ")
    animal=input("Enter an animal : ")
    place=input("Enter a place you like : ")
    food=input("Enter a food : ")

    madlib=f'\n💖 One sunny day, a {adjective} unicorn with a {colour} mane met a {animal} 😊. \nTogether they traveled to {place} to find the world\'s biggest {food} 🥭🍎. \nWhen they found it, they threw a giant party and everyone danced until sunset! 🌇'
    return madlib
    

def Dinosaur_Birthday():
    
    dinosaur_name=input("Enter dinosaur name : ")
    food=input("Enter a food : ")
    adjective=input("Enter an adjective : ")
    animal=input("Enter an animal you like : ")
    verb=input("Enter a verb : ")

    madlib=f'\nToday was {dinosaur_name}\'s birthday 🎂! \nFor the party, everyone ate {food}🍰. \nA very {adjective} {animal} arrived and started to {verb}. \nThe dinosaur laughed so hard that the birthday cake almost flew away! 😄'
    return madlib
    

def space_Puppy():
    puppy_name=input("Enter puppy name : ")
    planet=input("Enter a planet : ")
    adjective=input("Enter a feeling : ")
    verb=input("Enter a verb : ")
    item=input("Enter an object : ")

    madlib=f'\n🐕 A space puppy named {puppy_name} got lost near {planet} 🪐. \nThe puppy was feeling very {adjective}. \nSuddenly, it began to {verb} and found a magical {item}. \nThe puppy used it to fly back home and became a space hero! 🐕‍🦺'
    return madlib

while True:

    storyNumber=chooseStory()

    if storyNumber==1:
        print(Magical_Unicorn())
    elif storyNumber==2:
        print(Dinosaur_Birthday())
    elif storyNumber==3:
        print(space_Puppy())


    print("\nWoooooooow 🎉!!! You did a nice job kiddo 💖💖")

    play_again=input("\nDo you wanna play again sweetie 😊💖 (yes/no) : ").lower()
    if play_again=="no":
        print("\n👋 Thanks for playing! Have a magical day! 🌈")
        break



