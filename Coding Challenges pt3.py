#Coding Challenges

#Events calendar
def events_calendar_menu():
    #Lists of months and their events
    january = ["1st - New Years Day", "25th - Burns Night"]
    february = ["14th - Valentine's Day"]
    march = []
    april = ["1st - April Fools' Day"]
    may = []
    june = []
    july = []
    august = []
    september = []
    october = ["31st - Halloween"]
    november = ["5th - Bonfire night", "11th - Remembrance Day"]
    december = ["24th - Christmas Eve", "25th - Christmas Day", "26th - Boxing Day", "31st - New Years Eve"]

    print(".:Welcome to the events calendar menu:.\n")
    
    repeat = "Yes"
    while repeat != "No":

        #Menu style
        print("Option 1 = Display events")
        print("Option 2 = Add events")
        print("Option 3 = Delete events")
        print("Option 4 = Exit")
        option = int(input("Please choose an option."))
        
        if option == 1:
            #User can input the month they wish to view
            month = input("Please choose a month.")
            month = month.lower()
            #The month chosen by the user is outputted
            if month == "january":
                print(january)
            elif month == "february":
                print(february)
            elif month == "march":
                print(march)
            elif month == "april":
                print(april)
            elif month == "may":
                print(may)
            elif month == "june":
                print(june)
            elif month == "july":
                print(july)
            elif month == "august":
                print(august)
            elif month == "september":
                print(september)
            elif month == "october":
                print(october)
            elif month == "november":
                print(november)
            elif month == "december":
                print(december)
            else:
                print("Incorrect month selected.")
            repeat = "Yes"
        elif option == 2:
            month = input("Please choose a month.")
            month = month.lower()
            if month == "january":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                #The event inputted by the user is added to the list.
                january.append(event)
            elif month == "february":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                february.append(event)
            elif month == "march":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                march.append(event)
            elif month == "april":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                april.append(event)
            elif month == "may":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                may.append(event)
            elif month == "june":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                june.append(event)
            elif month == "july":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                july.append(event)
            elif month == "august":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                august.append(event)
            elif month == "september":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                september.append(event)
            elif month == "october":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                october.append(event)
            elif month == "november":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                november.append(event)
            elif month == "december":
                event = input("Please enter an event with the date. \nEnter in the form date - event. E.G. 12th - swimming")
                december.append(event)
            else:
                print("Incorrect month selected.")
            repeat = "Yes"
        elif option == 3:
            month = input("Please choose a month.")
            month = month.lower()
            if month == "january":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                #Event chosen by the user is removed.
                january.remove(delete)
            elif month == "february":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                february.remove(delete)
            elif month == "march":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                march.remove(delete)
            elif month == "april":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                april.remove(delete)
            elif month == "may":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                may.remove(delete)
            elif month == "june":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                june.remove(delete)
            elif month == "july":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                july.remove(delete)
            elif month == "august":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                august.remove(delete)
            elif month == "september":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                september.remove(delete)
            elif month == "october":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                october.remove(delete)
            elif month == "november":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                november.remove(delete)
            elif month == "december":
                delete = input("Please enter the event you wish to remove. \nEnter in the form date - event. E.G. 1st - dance")
                december.remove(delete)
            else:
                print("Incorrect month selected.")
            repeat = "Yes"
        #A way to exit the menu when you are done
        elif option == 4:
            print("Thank you for using the events calendar menu.")
            repeat = "No"
        #If the wrong number is inputted the code repeats
        else:
            print("Incorrect option inputted.")
            repeat = "Yes"

#Opening external file
def write():
    with open("diaryEntries.txt","w") as file:
        file.write("Welcome to the diary.\n\n")
        file.close()
write()

#Dear diary
def dear_diary():
    print("Welcome to your diary please feel free to add an entry or comment.")
    #Date stamp for the diary entry/comment
    date_stamp = input("Please enter the date for this entry/comment. enter in the format DD/MM/YYYY")
    #The diary entry created by the user
    entry = input("You may write diary entries or comments here:")
    #Adding the diary entry with date stamp to an external file - extension
    def append():
        with open("diaryEntries.txt","a") as file:
            file.write(date_stamp + "\n" + entry)
            file.close()
    append()

def menu():
    print("~~Welcome to the menu.~~\n")
    repeat = "Yes"
    while repeat != "No":

        #Options for the user to choose from
        print("Option 1 = Calendar events menu")
        print("Option 2 = Diary")
        print("Option 3 = Exit")
        option = int(input("Please choose an option."))

        if option == 1:
            events_calendar_menu()
            repeat = "Yes"
        elif option == 2:
            dear_diary()
            repeat = "Yes"
        elif option == 3:
            print("Thank you for using the menu.")
            repeat = "No"
        else:
            print("Incorrect option inputted.")
menu()
