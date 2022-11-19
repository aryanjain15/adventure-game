import sys


print("Welcome to this adventure game!")
ready =input("Are u ready for adventure? \n")
if ready == "Yes":
    print("Great! Time to buckle up your seat belts")
else:
    sys.exit()

print("The instructions for the game are: ")
print("You have 1 life if you mess up you DIE!")
print("There are 3 levels and if you clear all you survive the game and make it out alive")
print("GREAT! LETS START!")
print("You came across a river \n You have 2 options :")
print("You can either swing on the vines of trees ")
print("Use a bridge that is shaking")
print("Try and swim across")
first_opt = input("Which one will you choose to survive?")
if first_opt == "1":
    print("Sorry you died!")
    sys.exit()
elif first_opt == "2":
    print("Great You survived and moved on to the next level")
    print("You are now hungry :(")
    print("You have 3 options")
    print("Eat Wild berries!")
    print("Hunt a deer and eat it raw!")
    print("Survive on water!")
    second_opt = input("What will you choose?")
    if second_opt == "1":
        print("You survived")
        print("This is the last adventure if u survive this you win")
        print("There is a lion behind you \n What will you do ?")
        print("1. Run")
        print("Try and hide")
        print("Climb a tree!")
        print("Try and hide")
        third_opt = input("What option will you choose and what will you do?")
        if third_opt == "1":
            print("You died")
            sys.exit()
        elif third_opt == "2":
            print("You died")
            sys.exit()
        elif third_opt == "3":
            print("You won! and complted the challenge and the adventure game")
        if third_opt == "4":
            print("You died")
            sys.exit()
        else:
            print("Invalid input!")
    elif second_opt == "2":
        print("You died")
        sys.exit()
    elif second_opt == "3":
        print("You Died!")
        sys.exit()
    else:
        print("Invalid input!! TRY AGAIN !!")
        sys.exit()

elif first_opt == "3":
    print("You died!")
    sys.exit()
else:
    print("This is not a valid input TRY AGAIN")
    sys.exit()
##random correct answer here