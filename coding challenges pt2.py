#Two different coding challenges

import random

#Thief
def thief():
    attempt = 0
    pin_code = input("Please enter a four digit pin (numbers).")
    pin_attempt = ""
    #Repeat the code until the pin has been guessed
    while pin_code != pin_attempt:
        #Digit 1 of 4
        digit1 = random.randint(0,9)
        digit1 = str(digit1)
        #Digit 2 of 4
        digit2 = random.randint(0,9)
        digit2 = str(digit2)
        #Digit 3 of 4
        digit3 = random.randint(0,9)
        digit3 = str(digit3)
        #Digit 4 of 4
        digit4 = random.randint(0,9)
        digit4 = str(digit4)
        #Attempt of guessing the pin
        pin_attempt = digit1 + digit2 + digit3 + digit4
        print("The thief guessed that the pin was " + pin_attempt + ".")
        attempt = attempt + 1
        if pin_attempt == pin_code:
            print("The thief has guessed your pin.")
            print("It took the thief ", attempt,"attempts.")

#Thief - limited attempts
def thief_v2():
    attempt = 0
    pin_code = input("Please enter a four digit pin (numbers).")
    pin_attempt = ""
    num_attempts = int(input("Please enter the number of attempts."))
    for x in range (num_attempts):
        #Digit 1 of 4
        digit1 = random.randint(0,9)
        digit1 = str(digit1)
        #Digit 2 of 4
        digit2 = random.randint(0,9)
        digit2 = str(digit2)
        #Digit 3 of 4
        digit3 = random.randint(0,9)
        digit3 = str(digit3)
        #Digit 4 of 4
        digit4 = random.randint(0,9)
        digit4 = str(digit4)
        #Attempt of guessing the pin
        pin_attempt = digit1 + digit2 + digit3 + digit4
        print("The thief guessed that the pin was " + pin_attempt + ".")
        attempt = attempt + 1
        if pin_attempt == pin_code:
            print("The thief has guessed your pin.")
            break
        else:
            print("The thief hasn't guessed you pin.")

#Fibonacci sequence

def fibonacci(n):
    a = 0
    b = 1
    #Check that a number less than 0 hasn't been entered
    if n < 0:
        print("Incorrect input")
    #If 0 has been entered
    elif n == 0:
        print(0)
    #If 1 has been entered
    elif n == 1:
        print(1)
    else:
        for x in range(1, n):
            c = a + b
            a = b
            b = c
            print(b)
        

#Menu
def menu():
    repeat = "Yes"
    while repeat != "No":
        print("\nWelcome to the menu.\n")
        print("Option 1 = Thief - unlimited guesses")
        print("Option 2 = Thief v2 - limited guesses")
        print("Option 3 = Fibonacci")
        print("Option 4 = Exit")
        option = int(input("Please choose an option."))
        if option == 1:
            thief()
            repeat = "Yes"
        elif option == 2:
            #Extra - limited guesses for the thief to guess the pin
            thief_v2()
            repeat = "Yes"
        elif option == 3:
            #Extension - Allow the user to specify the number of places generated
            num = int(input("Please choose how many places you wish the fibonacci sequence to be calculated to."))
            fibonacci(n = num)
            repeat = "Yes"
        elif option == 4:
            print("Have a nice day.")
            repeat = "No"
        else:
            print("Incorrect input.")
            repeat = "Yes"
menu()
                      


