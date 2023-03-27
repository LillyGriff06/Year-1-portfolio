#Coding challlenge 1 - R@nd0m P@ssw0rd generator

import random
import csv

def write():
    with open("RandomPasswordGenerator.csv", "w") as file:
        file.write("R@nd0m P@ssw0rd generator \n")
        file.close()
write()

def random_password_generator():
    lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    symbols = ["!","£","$","%","@","&"]
    char1 = lower[random.randint(0,25)]
    char2 = symbols[random.randint(0,5)]
    char3 = symbols[random.randint(0,5)]
    char4 = upper[random.randint(0,25)]
    char5 = random.randint(0,9)
    char6 = lower[random.randint(0,25)]
    char7 = upper[random.randint(0,25)]
    char8 = lower[random.randint(0,25)]
    char9 = random.randint(0,9)
    char10 = lower[random.randint(0,25)]
    char11 = random.randint(0,9)
    char12 = upper[random.randint(0,25)]
    char5 = str(char5)
    char9 = str(char9)
    char11 = str(char11)
    random_password = char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12
    print("Your randomly generated password is " + random_password + ".")
    #Saving to file
    def append():
        with open("RandomPasswordGenerator.csv", "a") as file:
            file.write(random_password + "\n")
            file.close()
    append()


#Coding challenge 2 - Forwards and Backwards

def forwards_backwards():
    word = input("Please enter a word to check if it is the same backwards and forwards.")
    backwards = word[::-1]
    print("The word you entered is " + word + ".")
    print("Your word reversed is " + backwards + ".")
    if word == backwards:
        print("Your word is the same forwards and backwards.")
    else:
        print("Your word is not the same forwards and backwords.")


#Menu

def menu():
    repeat = "Y"
    while repeat != "N":
        print("Option 1 = random password generator")
        print("Option 2 = forwards and backwards")
        print("Option 3 = exit")
        option = int(input("Please enter an option."))
        if option == 1:
            random_password_generator()
            repeat = "Y"
        elif option == 2:
            forwards_backwards()
            repeat = "Y"
        elif option == 3:
            repeat = "N"
        else:
            print("Incorrect option inputted.")
            repeat = "Y"
menu()
