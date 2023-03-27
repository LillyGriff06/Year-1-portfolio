#Hotel management system

#CSV file
import csv
def write():
    with open ("hotel_management.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Forename", "Surname", "Phone number", "Email", "Address", "Card number", "Room number"])
        file.close()


#Customer details
def customerDetails():
    def name():
        global forename
        global surname
        forename = input("Please enter the customer's forename.")
        surname = input("Please enter the customer's surname.")
    name()
    def contact():
        global phoneNumber
        global email
        phoneNumber = int(input("Please enter the customer's phone number."))
        email = input("Please enter the customer's email address.")
    contact()
    def homeAddress():
        global address
        address = input("Please enter the customer's address.")
    homeAddress()
    def payment():
        global cardNumber
        cardNumber = int(input("Please enter your 16 digit debit card number."))
    payment()
        
#Room details
def roomDetails():
    roomTypes = ["Single", "Double", "Studio", "Family", "Standard-suite", "Royal-suite"]
    print(roomTypes)
    chosen = input("Choose a room type.")
    if chosen == "Single" or chosen == "single":
        price = 10.00
        print("A single room costs £", price, "per night.")
    elif chosen == "Double" or chosen == "double":
        price = 20.00
        print("A double room costs £", price, "per night.")
    elif chosen == "Studio" or chosen == "studio":
        price = 40.00
        print("A studio room costs £", price, "per night.")
    elif chosen == "Family" or chosen == "family":
        price = 55.00
        print("A family room costs £", price, "per night.")
    elif chosen == "Standard-suite" or chosen == "standard-suite":
        price = 70.00
        print("A standard suite costs £", price, "per night")
    elif chosen == "Royal-suite" or chosen == "royal-suite":
        price = 95.00
        print("A royal suite costs £", price, "per night")
    else:
        print("Error: A room type hasn't been chosen.")

#Rooms in the hotel
def oneRoom():
    global roomOneType
    global roomOnePrice
    global roomOneVacant
    global roomOneDescription
    roomOneType = "Single"
    roomOnePrice = 12.00
    roomOneVacant = "Yes"
    roomOneDescription = "Room 1 is a single room suitable for a person staying alone. The room comes with a single bed, a closet, a desk and a bathroom. The bathroom comes with both a bath and a shower. This room costs more than a standard single room because of the amazing view it provides."
    print("\n Room type: ", roomOneType,"\n Price: £", roomOnePrice, "\n Vacant: ", roomOneVacant, "\n Description: ", roomOneDescription)

def twoRoom():
    global roomTwoType
    global roomTwoPrice
    global roomTwoVacant
    global roomTwoDescription
    roomTwoType = "Single"
    roomTwoPrice = 10.00
    roomTwoVacant = "Yes"
    roomTwoDescription = "Room 2 is a single room suitable for a person staying alone. The room comes with a single bed, a closet, a desk and a bathroom. The bathroom comes with both a bath and a shower."
    print("\n Room type: ", roomTwoType,"\n Price: £", roomTwoPrice, "\n Vacant: ", roomTwoVacant, "\n Description: ", roomTwoDescription)
    
def threeRoom():
    global roomThreeType
    global roomThreePrice
    global roomThreeVacant
    global roomThreeDescription
    roomThreeType = "Double"
    roomThreePrice = 20.00
    roomThreeVacant = "Yes"
    roomThreeDescription = "Room 3 is a double room suitable for two people to stay together. The room comes with two single beds, a closet, a desk and a bathroom. The bathroom comes with both a bath and a shower."
    print("\n Room type: ", roomThreeType,"\n Price: £", roomThreePrice, "\n Vacant: ", roomThreeVacant, "\n Description: ", roomThreeDescription)

def fourRoom():
    global roomFourType
    global roomFourPrice
    global roomFourVacant
    global roomFourDescription
    roomFourType = "Double"
    roomFourPrice = 20.00
    roomFourVacant = "Yes"
    roomFourDescription = "Room 4 is a double room suitable for two people to stay together. The room comes with a double bed, a closet, a desk and a bathroom. The bathroom comes with both a bath and a shower."
    print("\n Room type: ", roomFourType,"\n Price: £", roomFourPrice, "\n Vacant: ", roomFourVacant, "\n Description: ", roomFourDescription)

def fiveRoom():
    global roomFiveType
    global roomFivePrice
    global roomFiveVacant
    global roomFiveDescription
    roomFiveType = "Studio"
    roomFivePrice = 40.00
    roomFiveVacant = "Yes"
    roomFiveDescription = "Room 5 is a studio room suitable for 1-4 people to stay. The room has two double beds that can be turned into couches. It also comes with a closet, a desk, a kitchenette and a bathroom. The bathroom comes with both a bath and a shower."
    print("\n Room type: ", roomFiveType,"\n Price: £", roomFivePrice, "\n Vacant: ", roomFiveVacant, "\n Description: ", roomFiveDescription)
    
def sixRoom():
    global roomSixType
    global roomSixPrice
    global roomSixVacant
    global roomSixDescription
    roomSixType = "Family"
    roomSixPrice = 55.00
    roomSixVacant = "Yes"
    roomSixDescription = "Room 6 is a family room suitable for a family with children of varying ages to stay. The room comes with a double bed, two single beds, a cot, two closets, a desk and a bathroom. The bathroom comes with both a bath and a shower."
    print("\n Room type: ", roomSixType,"\n Price: £", roomSixPrice, "\n Vacant: ", roomSixVacant, "\n Description: ", roomSixDescription)
    
def sevenRoom():
    global roomSevenType
    global roomSevenPrice
    global roomSevenVacant
    global roomSevenDescription
    roomSevenType = "Standard-suite"
    roomSevenPrice = 70.00
    roomSevenVacant = "Yes"
    roomSevenDescription = "Room 7 is a standard suite suitable for 1-6 people to stay. The suite is separated into four sections. These sections are two sleeping areas (each with a single and double bed), a living area and a bathroom. The bathroom comes with both a bath and a shower."
    print("\n Room type: ", roomSevenType,"\n Price: £", roomSevenPrice, "\n Vacant: ", roomSevenVacant, "\n Description: ", roomSevenDescription)
    
def eightRoom():
    global roomEightType
    global roomEightPrice
    global roomEightVacant
    global roomEightDescription
    roomEightType = "Royal-suite"
    roomEightPrice = 95.00
    roomEightVacant = "Yes"
    roomEightDescription = "Room 8 is a royal suite suitable for 1-8 people to stay. The suite is separated into multiple sections. These sections are four sleeping areas (each with double bed), a living area and two lavish bathroom. The each bathroom comes with a bath, a shower, heated floors and high-end/lush towels. The living area has a fireplace with concierge services so you don't need to light it yourself. The sleeping area come with deluxe pillows and mattresses, a tv, a closet, a desk and a safe."
    print("\n Room type: ", roomEightType,"\n Price: £", roomEightPrice, "\n Vacant: ", roomEightVacant, "\n Description: ", roomEightDescription)
    

#Booking system   
def booking():
    again="Yes"
    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
    while roomChoice > 0 and roomChoice < 9:
        while again != "No":
            if roomChoice == 1:
                roomOneVacant = "Yes"
                oneRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomOneVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomOnePrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append1():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 1"])
                                    file.close()
                            append1()
                            roomOneVacant == "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms.")) 
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 2:
                roomTwoVacant = "Yes"
                twoRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomTwoVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomTwoPrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append2():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 2"])
                                    file.close()
                            append2()
                            roomTwoVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 3:
                roomThreeVacant = "Yes"
                threeRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomThreeVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomThreePrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append3():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 3"])
                                    file.close()
                            append3()
                            roomThreeVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 4:
                roomFourVacant = "Yes"
                fourRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomFourVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomFourPrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append4():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 4"])
                                    file.close()
                            append4()
                            roomFourVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 5:
                roomFiveVacant = "Yes"
                fiveRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomFiveVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomFivePrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append5():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 5"])
                                    file.close()
                            append5()
                            roomFiveVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 6:
                roomSixVacant = "Yes"
                sixRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomSixVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomSixPrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append6():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 6"])
                                    file.close()
                            append6()
                            roomSixVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 7:
                roomSevenVacant = "Yes"
                sevenRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomSevenVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomSevenPrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append7():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 7"])
                                    file.close()
                            append7()
                            roomSevenVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
            if roomChoice == 8:
                roomEightVacant = "Yes"
                eightRoom()
                book = input("Would you like to book this room? Enter Y or N.")
                if book == "Y":
                    if roomEightVacant == "Yes":
                        again = "No"
                        duration = int(input("How many night do you wish to stay?"))
                        totalPrice = duration * roomEightPrice
                        print("The total cost for your stay will be £", totalPrice)
                        confirm = input("Are you sure you would like to book this room? Enter Y or N.")
                        if confirm == "Y":
                            customerDetails()
                            def append8():
                                with open ("hotel_management.csv", "a") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([forename, surname, phoneNumber, email, address, cardNumber, "Room 8"])
                                    file.close()
                            append8()
                            roomEightVacant = "No"
                            again = input("Would you like to book another room?")
                        else:
                            roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                    else:
                        again = "Yes"
                        print("This room is not vacant please choose another.")
                else:
                    roomChoice = int(input("Please enter the number of the room you would like to look at. There are 8 rooms."))
                        
            

def read():
    with open ("hotel_management.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        
#Main menu

def menu():
    repeat = "Y"
    print("Welcome to the Artemis Hotel's management system.")
    user = input("Are you a hotel manager or a customer?")
    while repeat == "Y":
        if user == "customer":
            write()
            print("Option 1 - Enter your details")
            print("Option 2 - Room Prices")
            print("Option 3 - Booking a room")
            option = int(input("Please choose one of the options."))
            if option == 1:
                customerDetails()
                repeat = input("Would you like to choose another option? Enter Y or N.")
            if option == 2:
                roomDetails()
                repeat = input("Would you like to choose another option? Enter Y or N.")
            if option == 3:
                booking()
                repeat = input("Would you like to choose another option? Enter Y or N.")
        elif user == "hotel manager":
            print("Option 1 - Display booking records")
            print("Option 2 - Entering a customers booking details")
            option = int(input("Please choose one of the options."))
            if option == 1:
                read()
                repeat = input("Would you like to choose another option? Enter Y or N.")
            if option == 2:
                booking()
                repeat = input("Would you like to choose another option? Enter Y or N.")
        else:
            print("You have entered invalid data.")
            user = input("Are you a hotel manager or a customer?")
            repeat = "Y"
menu()
            
