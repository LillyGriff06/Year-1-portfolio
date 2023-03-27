import csv

def write():
        with open("TutorGroupProgramProject.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Forename", "Surname", "Student ID", "Date of birth", "Address", "Phone number", "Email", "Gender", "Tutor group"])
write()
    
def login():
    global correctLogin
    correctLogin = False
    while correctLogin == False:
        usernameAttempt=input("Username: \n")
        passwordAttempt=input("Password: \n")
        username="LeemanTRS"
        password="TRSLeeman123"
        if usernameAttempt == username:
            if passwordAttempt == password:
                print("The username and password are correct.")
                correctLogin = True
            else:
                print("Incorrect username or password.")
                correctLogin = False
        else:
            print("Incorrect username or password.")
            correctLogin = False
login()

def name():
    correctName = False
    while correctName == False:
        global forename
        global surname
        forename=input("Please enter the student's forename.")
        surname=input("Please enter the student's surname.")
        if len(forename) > 0:
            if len(surname) > 0:
                print("The forename and surname is correct.")
                correctName = True
            else:
                print("Incorrect forename or surname.")
                correctName = False
        else:
            print("Incorrect forname or surname.")
            correctName = False


def id():
    correctID = False
    while correctID == False:
        global studentID
        studentID=input("Please enter the Student's unique ID number.")
        if len(studentID) > 0:
            print("The student's unique ID number is correct.")
            correctID = True
        else:
            print("The student's unique ID number is incorrect")
            correctID = False


def dateofbirth():
    correctDOB = False
    while correctDOB == False:
        global dob
        dob=input("Please enter the student's date of birth in the format DD/MM/YY.")
        if len(dob)== 8:
            print("The student's date of birth is correct.")
            correctDOB = True
        else:
            print("The student's date of birth is incorrect.")
            correctDOB = False


def homeAddress():
    correctAddress = False
    while correctAddress == False:
        global address
        address=input("Please enter the student's home address.")
        if len(address) > 0:
            print("The student's address is correct.")
            correctAddress = True
        else:
            print("The student's address is incorrect.")
            correctAddress = False


def contact():
    correctContact = False
    while correctContact == False:
        global phoneNumber
        global email
        phoneNumber=int(input("Please enter the Student's home phone number."))
        email=input("Please enter the student's unique school email address.")
        phoneNumber=str(phoneNumber)
        if len(email) > 0:
            print("The student's school email address is correct.")
            correctContact = True
        else:
            print("Incorrect school email address.")
            correctContact = False


def studentgender():
    correctGender = False
    while correctGender == False:
        global gender
        gender=input("Please enter the student's gender.")
        if len(gender) > 0:
            print("The gender entered is correct.")
            correctGender = True
        else:
            print("The gender entered is incorrect.")
            correctGender = False


def tutor():
    correctGroup = False
    while correctGroup == False:
        global tutorGroup
        tutorGroup=input("Please enter the student's tutor group.")
        if len(tutorGroup) > 0:
            print("The tutor group entered is correct.")
            correctGroup = True
        else:
            print("The tutor group entered is incorrect.")
            correctGroup = False


def details():
        students = 5
        while students !=0:
                name()
                id()
                dateofbirth()
                homeAddress()
                contact()
                studentgender()
                tutor()
                def append():
                        with open("TutorGroupProgramProject.csv", "a") as file:
                                writer = csv.writer(file)
                                writer.writerow([forename, surname, studentID, dob, address, phoneNumber, email, gender, tutorGroup])
                                file.close()
                append()
                students=students-1

        
        
def reports():
        report1="\nDisplay of menu - The menu is displayed in a user friendly way so that it is easy for anyone to use. The menu explains what to enter to access each option."
        print(report1)
        report2="\nNumber of students - Each time a user chooses the option to add student details they must add 5 students."
        print(report2)
        report3="\nMales and females - The numbers of males and females in a form can vary for different forms."
        print(report3)
    

def menu():
    correctOption = False
    while correctOption == False:
        print("\nWhat would you like to do today.")
        print("Add student details = 1")
        print("Display student details = 2")
        print("Display reports = 3")
        option=int(input("Please choose an option by entering the number."))
        if option > 3:
            print("Please enter a number between 1 and 3")
            correctOption = False
        else:
            correctOption = True
    if option == 1:
        details()
    if option == 2:
        def read():
            with open("TutorGroupProgramProject.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        read()
    if option == 3:
        reports()


logout = "N"
while logout == "N":
    menu()
    logout=input("Would you like to log out of the system. \n Enter Y for yes or N for no.")
