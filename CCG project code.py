import random

print("Welcome to the CCG.")
def repeat():
    repeat="Yes"
    while repeat != "No":
        def win():
            round=0
            while round != 6:
                win=False
                playerPoints=0
                computerPoints=0
                def colours():
                    purple=1
                    blue=2
                    red=3
                    yellow=4
                    green=5
                    print("purple =", purple, ", blue =", blue, ", red =", red, ", yellow =", yellow, "and green =", green)
                colours()
                while win != True:
                    valid=False
                    while valid != True:
                        playerChoice=int(input("Please enter the number that matches your colour."))
                        if 0 < playerChoice < 6:
                            valid=True
                        else:
                            valid=False
                            print("Please enter a number between 1 and 5.")
                    computerChoice=random.randint(1,5)
                    print("The computer has entered ", computerChoice)
                    if playerChoice != computerChoice:
                        playerPoints=playerPoints+1
                        win=True
                        round += 1
                        print("You have gained a point")
                    else:
                        computerPoints=computerPoints+1
                        win=False
                        round += 1
                        print("The computer has gained a point")
        win()
        repeat=input("You have won. \nWould you like to continue. Enter Yes or No.")
        if repeat == "No":
            print("Thanks for playing.")
repeat()
