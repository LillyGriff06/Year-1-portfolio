#Hockey game project code


import csv

def write():
    with open ("HockeyTeams.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Team", "Player name", "Attack value", "Defence value"])
        file.close()
write()
    
#Team details

def team_1_details():
    global t1_p1_attack
    global t1_p1_defence
    global t1_p2_attack
    global t1_p2_defence
    global t1_p3_attack
    global t1_p3_defence
    global t1_p4_attack
    global t1_p4_defence
    global t1_p5_attack
    global t1_p5_defence
    global t1_p6_attack
    global t1_p6_defence
    correct = "No"
    while correct != "Yes":
        t1_p1_name = input("Please enter the name of player 1 on team 1.")
        t1_p1_attack = int(input("Please enter the attack value of player 1 on team 1."))
        t1_p1_defence = int(input("Please enter the defence value of player 1 on team 1."))
        
        t1_p2_name = input("Please enter the name of player 2 on team 1.")
        t1_p2_attack = int(input("Please enter the attack value of player 2 on team 1."))
        t1_p2_defence = int(input("Please enter the defence value of player 2 on team 1."))
        
        t1_p3_name = input("Please enter the name of player 3 on team 1.")
        t1_p3_attack = int(input("Please enter the attack value of player 3 on team 1."))
        t1_p3_defence = int(input("Please enter the defence value of player 3 on team 1."))
        
        t1_p4_name = input("Please enter the name of player 4 on team 1.")
        t1_p4_attack = int(input("Please enter the attack value of player 4 on team 1."))
        t1_p4_defence = int(input("Please enter the defence value of player 4 on team 1."))
        
        t1_p5_name = input("Please enter the name of player 5 on team 1.")
        t1_p5_attack = int(input("Please enter the attack value of player 5 on team 1."))
        t1_p5_defence = int(input("Please enter the defence value of player 5 on team 1."))

        t1_p6_name = input("Please enter the name of player 6 on team 1.")
        t1_p6_attack = int(input("Please enter the attack value of player 6 on team 1."))
        t1_p6_defence = int(input("Please enter the defence value of player 6 on team 1."))

        t1_p1_attack_defence = t1_p1_attack + t1_p1_defence
        t1_p2_attack_defence = t1_p2_attack + t1_p2_defence
        t1_p3_attack_defence = t1_p3_attack + t1_p3_defence
        t1_p4_attack_defence = t1_p4_attack + t1_p4_defence
        t1_p5_attack_defence = t1_p5_attack + t1_p5_defence
        t1_p6_attack_defence = t1_p6_attack + t1_p6_defence

        t1_attack_defence = t1_p1_attack_defence + t1_p2_attack_defence + t1_p3_attack_defence + t1_p4_attack_defence + t1_p5_attack_defence + t1_p6_attack_defence

        if t1_p1_attack > 10 or t1_p1_defence > 7:
            print("Attack/defence value is too high. \n Please enter a new value.")
            correct = "No"
        else:
            if t1_p2_attack > 10 or t1_p2_defence > 7:
                print("Attack/defence value is too high. \n Please enter a new value.")
                correct = "No"
            else:
                if t1_p3_attack > 10 or t1_p3_defence > 7:
                    print("Attack/defence value is too high. \n Please enter a new value.")
                    correct = "No"
                else:
                    if t1_p4_attack > 10 or t1_p4_defence > 7:
                        print("Attack/defence value is too high. \n Please enter a new value.")
                        correct = "No"
                    else:
                        if t1_p5_attack > 10 or t1_p5_defence > 7:
                            print("Attack/defence value is too high. \n Please enter a new value.")
                            correct = "No"
                        else:
                            if t1_p6_attack > 10 or t1_p6_defence > 7:
                                print("Attack/defence value is too high. \n Please enter a new value.")
                                correct = "No"
                            else:
                                if t1_attack_defence < 35:
                                    print("The total attack + defence values of the team is too low. \n Please enter new values.")
                                    correct = "No"
                                elif t1_attack_defence > 35:
                                    print("The total attack + defence values of the team is too high. \n Please enter new values.")
                                    correct = "No"
                                else:
                                    correct = "Yes"
                
    def append1():
        with open ("HockeyTeams.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow(["Team 1", t1_p1_name, t1_p1_attack, t1_p1_defence])
            writer.writerow(["Team 1", t1_p2_name, t1_p2_attack, t1_p2_defence])
            writer.writerow(["Team 1", t1_p3_name, t1_p3_attack, t1_p3_defence])
            writer.writerow(["Team 1", t1_p4_name, t1_p4_attack, t1_p4_defence])
            writer.writerow(["Team 1", t1_p5_name, t1_p5_attack, t1_p5_defence])
            writer.writerow(["Team 1", t1_p6_name, t1_p6_attack, t1_p6_defence])
            file.close()
    append1()


def team_2_details():
    global t2_p1_attack
    global t2_p1_defence
    global t2_p2_attack
    global t2_p2_defence
    global t2_p3_attack
    global t2_p3_defence
    global t2_p4_attack
    global t2_p4_defence
    global t2_p5_attack
    global t2_p5_defence
    global t2_p6_attack
    global t2_p6_defence
    correct = "No"
    while correct != "Yes":
        t2_p1_name = input("Please enter the name of player 1 on team 2.")
        t2_p1_attack = int(input("Please enter the attack value of player 1 on team 2."))
        t2_p1_defence = int(input("Please enter the defence value of player 1 on team 2."))
        
        t2_p2_name = input("Please enter the name of player 2 on team 2.")
        t2_p2_attack = int(input("Please enter the attack value of player 2 on team 2."))
        t2_p2_defence = int(input("Please enter the defence value of player 2 on team 2."))
        
        t2_p3_name = input("Please enter the name of player 3 on team 2.")
        t2_p3_attack = int(input("Please enter the attack value of player 3 on team 2."))
        t2_p3_defence = int(input("Please enter the defence value of player 3 on team 2."))
        
        t2_p4_name = input("Please enter the name of player 4 on team 2.")
        t2_p4_attack = int(input("Please enter the attack value of player 4 on team 2."))
        t2_p4_defence = int(input("Please enter the defence value of player 4 on team 2."))
        
        t2_p5_name = input("Please enter the name of player 5 on team 2.")
        t2_p5_attack = int(input("Please enter the attack value of player 5 on team 2."))
        t2_p5_defence = int(input("Please enter the defence value of player 5 on team 2."))

        t2_p6_name = input("Please enter the name of player 6 on team 2.")
        t2_p6_attack = int(input("Please enter the attack value of player 6 on team 2."))
        t2_p6_defence = int(input("Please enter the defence value of player 6 on team 2."))

        t2_p1_attack_defence = t2_p1_attack + t2_p1_defence
        t2_p2_attack_defence = t2_p2_attack + t2_p2_defence
        t2_p3_attack_defence = t2_p3_attack + t2_p3_defence
        t2_p4_attack_defence = t2_p4_attack + t2_p4_defence
        t2_p5_attack_defence = t2_p5_attack + t2_p5_defence
        t2_p6_attack_defence = t2_p6_attack + t2_p6_defence

        t2_attack_defence = t2_p1_attack_defence + t2_p2_attack_defence + t2_p3_attack_defence + t2_p4_attack_defence + t2_p5_attack_defence + t2_p6_attack_defence

        if t2_p1_attack > 10 or t2_p1_defence > 7:
            print("Attack/defence value is too high. \n Please enter a new value.")
            correct = "No"
        else:
            if t2_p2_attack > 10 or t2_p2_defence > 7:
                print("Attack/defence value is too high. \n Please enter a new value.")
                correct = "No"
            else:
                if t2_p3_attack > 10 or t2_p3_defence > 7:
                    print("Attack/defence value is too high. \n Please enter a new value.")
                    correct = "No"
                else:
                    if t2_p4_attack > 10 or t2_p4_defence > 7:
                        print("Attack/defence value is too high. \n Please enter a new value.")
                        correct = "No"
                    else:
                        if t2_p5_attack > 10 or t2_p5_defence > 7:
                            print("Attack/defence value is too high. \n Please enter a new value.")
                            correct = "No"
                        else:
                            if t2_p6_attack > 10 or t2_p6_defence > 7:
                                print("Attack/defence value is too high. \n Please enter a new value.")
                                correct = "No"
                            else:
                                if t2_attack_defence < 35:
                                    print("The total attack + defence values of the team is too low. \n Please enter new values.")
                                    correct = "No"
                                elif t2_attack_defence > 35:
                                    print("The total attack + defence values of the team is too high. \n Please enter new values.")
                                    correct = "No"
                                else:
                                    correct = "Yes"
                
    def append2():
        with open ("HockeyTeams.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow(["Team 2", t2_p1_name, t2_p1_attack, t2_p1_defence])
            writer.writerow(["Team 2", t2_p2_name, t2_p2_attack, t2_p2_defence])
            writer.writerow(["Team 2", t2_p3_name, t2_p3_attack, t2_p3_defence])
            writer.writerow(["Team 2", t2_p4_name, t2_p4_attack, t2_p4_defence])
            writer.writerow(["Team 2", t2_p5_name, t2_p5_attack, t2_p5_defence])
            writer.writerow(["Team 2", t2_p6_name, t2_p6_attack, t2_p6_defence])
            file.close()
    append2()


def team_3_details():
    global t3_p1_attack
    global t3_p1_defence
    global t3_p2_attack
    global t3_p2_defence
    global t3_p3_attack
    global t3_p3_defence
    global t3_p4_attack
    global t3_p4_defence
    global t3_p5_attack
    global t3_p5_defence
    global t3_p6_attack
    global t3_p6_defence
    correct = "No"
    while correct != "Yes":
        t3_p1_name = input("Please enter the name of player 1 on team 3.")
        t3_p1_attack = int(input("Please enter the attack value of player 1 on team 3."))
        t3_p1_defence = int(input("Please enter the defence value of player 1 on team 3."))
        
        t3_p2_name = input("Please enter the name of player 2 on team 3.")
        t3_p2_attack = int(input("Please enter the attack value of player 2 on team 3."))
        t3_p2_defence = int(input("Please enter the defence value of player 2 on team 3."))
        
        t3_p3_name = input("Please enter the name of player 3 on team 3.")
        t3_p3_attack = int(input("Please enter the attack value of player 3 on team 3."))
        t3_p3_defence = int(input("Please enter the defence value of player 3 on team 3."))
        
        t3_p4_name = input("Please enter the name of player 4 on team 3.")
        t3_p4_attack = int(input("Please enter the attack value of player 4 on team 3."))
        t3_p4_defence = int(input("Please enter the defence value of player 4 on team 3."))
        
        t3_p5_name = input("Please enter the name of player 5 on team 3.")
        t3_p5_attack = int(input("Please enter the attack value of player 5 on team 3."))
        t3_p5_defence = int(input("Please enter the defence value of player 5 on team 3."))

        t3_p6_name = input("Please enter the name of player 6 on team 3.")
        t3_p6_attack = int(input("Please enter the attack value of player 6 on team 3."))
        t3_p6_defence = int(input("Please enter the defence value of player 6 on team 3."))

        t3_p1_attack_defence = t3_p1_attack + t3_p1_defence
        t3_p2_attack_defence = t3_p2_attack + t3_p2_defence
        t3_p3_attack_defence = t3_p3_attack + t3_p3_defence
        t3_p4_attack_defence = t3_p4_attack + t3_p4_defence
        t3_p5_attack_defence = t3_p5_attack + t3_p5_defence
        t3_p6_attack_defence = t3_p6_attack + t3_p6_defence

        t3_attack_defence = t3_p1_attack_defence + t3_p2_attack_defence + t3_p3_attack_defence + t3_p4_attack_defence + t3_p5_attack_defence + t3_p6_attack_defence

        if t3_p1_attack > 10 or t3_p1_defence > 7:
            print("Attack/defence value is too high. \n Please enter a new value.")
            correct = "No"
        else:
            if t3_p2_attack > 10 or t3_p2_defence > 7:
                print("Attack/defence value is too high. \n Please enter a new value.")
                correct = "No"
            else:
                if t3_p3_attack > 10 or t3_p3_defence > 7:
                    print("Attack/defence value is too high. \n Please enter a new value.")
                    correct = "No"
                else:
                    if t3_p4_attack > 10 or t3_p4_defence > 7:
                        print("Attack/defence value is too high. \n Please enter a new value.")
                        correct = "No"
                    else:
                        if t3_p5_attack > 10 or t3_p5_defence > 7:
                            print("Attack/defence value is too high. \n Please enter a new value.")
                            correct = "No"
                        else:
                            if t3_p6_attack > 10 or t3_p6_defence > 7:
                                print("Attack/defence value is too high. \n Please enter a new value.")
                                correct = "No"
                            else:
                                if t3_attack_defence < 35:
                                    print("The total attack + defence values of the team is too low. \n Please enter new values.")
                                    correct = "No"
                                elif t3_attack_defence > 35:
                                    print("The total attack + defence values of the team is too high. \n Please enter new values.")
                                    correct = "No"
                                else:
                                    correct = "Yes"
                
    def append3():
        with open ("HockeyTeams.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow(["Team 3", t3_p1_name, t3_p1_attack, t3_p1_defence])
            writer.writerow(["Team 3", t3_p2_name, t3_p2_attack, t3_p2_defence])
            writer.writerow(["Team 3", t3_p3_name, t3_p3_attack, t3_p3_defence])
            writer.writerow(["Team 3", t3_p4_name, t3_p4_attack, t3_p4_defence])
            writer.writerow(["Team 3", t3_p5_name, t3_p5_attack, t3_p5_defence])
            writer.writerow(["Team 3", t3_p6_name, t3_p6_attack, t3_p6_defence])
            file.close()
    append3()


def team_4_details():
    correct = "No"
    while correct != "Yes":
        t4_p1_name = input("Please enter the name of player 1 on team 4.")
        t4_p1_attack = int(input("Please enter the attack value of player 1 on team 4."))
        t4_p1_defence = int(input("Please enter the defence value of player 1 on team 4."))
        
        t4_p2_name = input("Please enter the name of player 2 on team 4.")
        t4_p2_attack = int(input("Please enter the attack value of player 2 on team 4."))
        t4_p2_defence = int(input("Please enter the defence value of player 2 on team 4."))
        
        t4_p3_name = input("Please enter the name of player 3 on team 4.")
        t4_p3_attack = int(input("Please enter the attack value of player 3 on team 4."))
        t4_p3_defence = int(input("Please enter the defence value of player 3 on team 4."))
        
        t4_p4_name = input("Please enter the name of player 4 on team 4.")
        t4_p4_attack = int(input("Please enter the attack value of player 4 on team 4."))
        t4_p4_defence = int(input("Please enter the defence value of player 4 on team 4."))
        
        t4_p5_name = input("Please enter the name of player 5 on team 4.")
        t4_p5_attack = int(input("Please enter the attack value of player 5 on team 4."))
        t4_p5_defence = int(input("Please enter the defence value of player 5 on team 4."))

        t4_p6_name = input("Please enter the name of player 6 on team 4.")
        t4_p6_attack = int(input("Please enter the attack value of player 6 on team 4."))
        t4_p6_defence = int(input("Please enter the defence value of player 6 on team 4."))

        t4_p1_attack_defence = t4_p1_attack + t4_p1_defence
        t4_p2_attack_defence = t4_p2_attack + t4_p2_defence
        t4_p3_attack_defence = t4_p3_attack + t4_p3_defence
        t4_p4_attack_defence = t4_p4_attack + t4_p4_defence
        t4_p5_attack_defence = t4_p5_attack + t4_p5_defence
        t4_p6_attack_defence = t4_p6_attack + t4_p6_defence

        t4_attack_defence = t4_p1_attack_defence + t4_p2_attack_defence + t4_p3_attack_defence + t4_p4_attack_defence + t4_p5_attack_defence + t4_p6_attack_defence

        if t4_p1_attack > 10 or t1_p4_defence > 7:
            print("Attack/defence value is too high. \n Please enter a new value.")
            correct = "No"
        else:
            if t4_p2_attack > 10 or t4_p2_defence > 7:
                print("Attack/defence value is too high. \n Please enter a new value.")
                correct = "No"
            else:
                if t4_p3_attack > 10 or t4_p3_defence > 7:
                    print("Attack/defence value is too high. \n Please enter a new value.")
                    correct = "No"
                else:
                    if t4_p4_attack > 10 or t4_p4_defence > 7:
                        print("Attack/defence value is too high. \n Please enter a new value.")
                        correct = "No"
                    else:
                        if t4_p5_attack > 10 or t4_p5_defence > 7:
                            print("Attack/defence value is too high. \n Please enter a new value.")
                            correct = "No"
                        else:
                            if t4_p6_attack > 10 or t4_p6_defence > 7:
                                print("Attack/defence value is too high. \n Please enter a new value.")
                                correct = "No"
                            else:
                                if t4_attack_defence < 35:
                                    print("The total attack + defence values of the team is too low. \n Please enter new values.")
                                    correct = "No"
                                elif t4_attack_defence > 35:
                                    print("The total attack + defence values of the team is too high. \n Please enter new values.")
                                    correct = "No"
                                else:
                                    correct = "Yes"
                
    def append4():
        with open ("HockeyTeams.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow(["Team 4", t4_p1_name, t4_p1_attack, t4_p1_defence])
            writer.writerow(["Team 4", t4_p2_name, t4_p2_attack, t4_p2_defence])
            writer.writerow(["Team 4", t4_p3_name, t4_p3_attack, t4_p3_defence])
            writer.writerow(["Team 4", t4_p4_name, t4_p4_attack, t4_p4_defence])
            writer.writerow(["Team 4", t4_p5_name, t4_p5_attack, t4_p5_defence])
            writer.writerow(["Team 4", t4_p6_name, t4_p6_attack, t4_p6_defence])
            file.close()
    append4()


def game():
    penalty_u1_team = 0
    penalty_u2_team = 0
    penalty_saved_u1 = 0
    penalty_saved_u2 = 0
    correct1 = "No"
    correct2 = "No"
    while correct1 != "Yes":
        u1_team = input("Please select the team you would like to use. Enter in this format: team 1")
        if u1_team == "team 1":
            print("Team 1 has been chosen.")
            correct1 = "Yes"
        elif u1_team == "team 2":
            print("Team 2 has been chosen.")
            correct1 = "Yes"
        elif u1_team == "team 3":
            print("Team 3 has been chosen.")
            correct1 = "Yes"
        elif u1_team == "team 4":
            print("Team 4 has been chosen.")
            correct1 = "Yes"
        else:
            print("Incorrect team chosen.")
            correct1 = "No"

    while correct2 != "Yes":
        u2_team = input("Please select the team you would like to use. Enter in this format: team 1")
        if u2_team == "team 1":
            if u1_team == u2_team:
                print("User 1 has already chosen this team. Please choose a new team.")
                correct2 = "No"
            else:
                print("Team 1 has been chosen.")
                correct2 = "Yes"
        elif u2_team == "team 2":
            if u1_team == u2_team:
                print("User 1 has already chosen this team. Please choose a new team.")
                correct2 = "No"
            else:
                print("Team 2 has been chosen.")
                correct2 = "Yes"
        elif u2_team == "team 3":
            if u1_team == u2_team:
                print("User 1 has already chosen this team. Please choose a new team.")
                correct2 = "No"
            else:
                print("Team 3 has been chosen.")
                correct2 = "Yes"
        elif u2_team == "team 4":
            if u1_team == u2_team:
                print("User 1 has already chosen this team. Please choose a new team.")
                correct2 = "No"
            else:
                print("Team 4 has been chosen.")
                correct2 = "Yes"
        else:
            print("Incorrect team chosen.")
            correct2 = "No"
    
    if u1_team == "team 1":
        u1_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct3 = "No"
        while correct3 != "Yes":
            if u1_goalkeeper == "player 1":
                goalkeeper_u1 = t1_p1_defence
                correct3 = "Yes"
            elif u1_goalkeeper == "player 2":
                goalkeeper_u1 = t1_p2_defence
                correct3 = "Yes"
            elif u1_goalkeeper == "player 3":
                goalkeeper_u1 = t1_p3_defence
                correct3 = "Yes"
            elif u1_goalkeeper == "player 4":
                goalkeeper_u1 = t1_p4_defence
                correct3 = "Yes"
            elif u1_goalkeeper == "player 5":
                goalkeeper_u1 = t1_p5_defence
                correct3 = "Yes"
            elif u1_goalkeeper == "player 6":
                goalkeeper_u1 = t1_p6_defence
                correct3 = "Yes"
            else:
                print("Incorrect input")
                correct3 = "No"
            
    elif u1_team == "team 2":
        u1_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct4 = "No"
        while correct4 != "Yes":
            if u1_goalkeeper == "player 1":
                goalkeeper_u1 = t2_p1_defence
                correct4 = "Yes"
            elif u1_goalkeeper == "player 2":
                goalkeeper_u1 = t2_p2_defence
                correct4 = "Yes"
            elif u1_goalkeeper == "player 3":
                goalkeeper_u1 = t2_p3_defence
                correct4 = "Yes"
            elif u1_goalkeeper == "player 4":
                goalkeeper_u1 = t2_p4_defence
                correct4 = "Yes"
            elif u1_goalkeeper == "player 5":
                goalkeeper_u1 = t2_p5_defence
                correct4 = "Yes"
            elif u1_goalkeeper == "player 6":
                goalkeeper_u1 = t2_p6_defence
                correct4 = "Yes"
            else:
                print("Incorrect input")
                correct4 = "No"
            
    elif u1_team == "team 3":
        u1_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct5 = "No"
        while correct5 != "Yes":
            if u1_goalkeeper == "player 1":
                goalkeeper_u1 = t3_p1_defence
                correct5 = "Yes"
            elif u1_goalkeeper == "player 2":
                goalkeeper_u1 = t3_p2_defence
                correct5 = "Yes"
            elif u1_goalkeeper == "player 3":
                goalkeeper_u1 = t3_p3_defence
                correct5 = "Yes"
            elif u1_goalkeeper == "player 4":
                goalkeeper_u1 = t3_p4_defence
                correct5 = "Yes"
            elif u1_goalkeeper == "player 5":
                goalkeeper_u1 = t3_p5_defence
                correct5 = "Yes"
            elif u1_goalkeeper == "player 6":
                goalkeeper_u1 = t3_p6_defence
                correct5 = "Yes"
            else:
                print("Incorrect input")
                correct5 = "No"

    elif u1_team == "team 4":
        u1_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct6 = "No"
        while correct6 != "Yes":
            if u1_goalkeeper == "player 1":
                goalkeeper_u1 = t4_p1_defence
                correct6 = "Yes"
            elif u1_goalkeeper == "player 2":
                goalkeeper_u1 = t4_p2_defence
                correct6 = "Yes"
            elif u1_goalkeeper == "player 3":
                goalkeeper_u1 = t4_p3_defence
                correct6 = "Yes"
            elif u1_goalkeeper == "player 4":
                goalkeeper_u1 = t4_p4_defence
                correct6 = "Yes"
            elif u1_goalkeeper == "player 5":
                goalkeeper_u1 = t4_p5_defence
                correct6 = "Yes"
            elif u1_goalkeeper == "player 6":
                goalkeeper_u1 = t4_p6_defence
                correct6 = "Yes"
            else:
                print("Incorrect input")
                correct6 = "No"

    if u2_team == "team 1":
        u2_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct7 = "No"
        while correct7 != "Yes":
            if u2_goalkeeper == "player 1":
                goalkeeper_u2 = t1_p1_defence
                correct7 = "Yes"
            elif u2_goalkeeper == "player 2":
                goalkeeper_u2 = t1_p2_defence
                correct7 = "Yes"
            elif u2_goalkeeper == "player 3":
                goalkeeper_u2 = t1_p3_defence
                correct7 = "Yes"
            elif u2_goalkeeper == "player 4":
                goalkeeper_u2 = t1_p4_defence
                correct7 = "Yes"
            elif u2_goalkeeper == "player 5":
                goalkeeper_u2 = t1_p5_defence
                correct7 = "Yes"
            elif u2_goalkeeper == "player 6":
                goalkeeper_u2 = t1_p6_defence
                correct7 = "Yes"
            else:
                print("Incorrect input")
                correct7 = "No"
            
    elif u2_team == "team 2":
        u2_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct8 = "No"
        while correct8 != "Yes":
            if u2_goalkeeper == "player 1":
                goalkeeper_u2 = t2_p1_defence
                correct8 = "Yes"
            elif u2_goalkeeper == "player 2":
                goalkeeper_u2 = t2_p2_defence
                correct8 = "Yes"
            elif u2_goalkeeper == "player 3":
                goalkeeper_u2 = t2_p3_defence
                correct8 = "Yes"
            elif u2_goalkeeper == "player 4":
                goalkeeper_u2 = t2_p4_defence
                correct8 = "Yes"
            elif u2_goalkeeper == "player 5":
                goalkeeper_u2 = t2_p5_defence
                correct8 = "Yes"
            elif u2_goalkeeper == "player 6":
                goalkeeper_u2 = t2_p6_defence
                correct8 = "Yes"
            else:
                print("Incorrect input")
                correct8 = "No"
            
    elif u2_team == "team 3":
        u2_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct9 = "No"
        while correct9 != "Yes":
            if u2_goalkeeper == "player 1":
                goalkeeper_u2 = t3_p1_defence
                correct9 = "Yes"
            elif u2_goalkeeper == "player 2":
                goalkeeper_u2 = t3_p2_defence
                correct9 = "Yes"
            elif u2_goalkeeper == "player 3":
                goalkeeper_u2 = t3_p3_defence
                correct9 = "Yes"
            elif u2_goalkeeper == "player 4":
                goalkeeper_u2 = t3_p4_defence
                correct9 = "Yes"
            elif u2_goalkeeper == "player 5":
                goalkeeper_u2 = t3_p5_defence
                correct9 = "Yes"
            elif u2_goalkeeper == "player 6":
                goalkeeper_u2 = t3_p6_defence
                correct9 = "Yes"
            else:
                print("Incorrect input")
                correct9 = "No"

    elif u2_team == "team 4":
        u2_goalkeeper = input("Please choose a goalkeeper. Enter in this format: player 0")
        correct0 = "No"
        while correct0 != "Yes":
            if u2_goalkeeper == "player 1":
                goalkeeper_u2 = t4_p1_defence
                correct0 = "Yes"
            elif u1_goalkeeper == "player 2":
                goalkeeper_u1 = t4_p2_defence
                correct6 = "Yes"
            elif u2_goalkeeper == "player 3":
                goalkeeper_u2 = t4_p3_defence
                correct0 = "Yes"
            elif u2_goalkeeper == "player 4":
                goalkeeper_u2 = t4_p4_defence
                correct0 = "Yes"
            elif u2_goalkeeper == "player 5":
                goalkeeper_u2 = t4_p5_defence
                correct0 = "Yes"
            elif u2_goalkeeper == "player 6":
                goalkeeper_u2 = t4_p6_defence
                correct0 = "Yes"
            else:
                print("Incorrect input")
                correct0 = "No"

#Playing the game

    if u2_team == "team 1":
        penalty1 = goalkeeper_u1 - t1_p1_attack
        if penalty1 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty2 = goalkeeper_u1 - t1_p2_attack
        if penalty2 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty3 = goalkeeper_u1 - t1_p3_attack
        if penalty3 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty4 = goalkeeper_u1 - t1_p4_attack
        if penalty4 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty5 = goalkeeper_u1 - t1_p5_attack
        if penalty5 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty6 = goalkeeper_u1 - t1_p6_attack
        if penalty6 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
            
    elif u2_team == "team 2":
        penalty1 = goalkeeper_u1 - t2_p1_attack
        if penalty1 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty2 = goalkeeper_u1 - t2_p2_attack
        if penalty2 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty3 = goalkeeper_u1 - t2_p3_attack
        if penalty3 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty4 = goalkeeper_u1 - t2_p4_attack
        if penalty4 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty5 = goalkeeper_u1 - t2_p5_attack
        if penalty5 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty6 = goalkeeper_u1 - t2_p6_attack
        if penalty6 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
            
    elif u2_team == "team 3":
        penalty1 = goalkeeper_u1 - t3_p1_attack
        if penalty1 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty2 = goalkeeper_u1 - t3_p2_attack
        if penalty2 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty3 = goalkeeper_u1 - t3_p3_attack
        if penalty3 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty4 = goalkeeper_u1 - t3_p4_attack
        if penalty4 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty5 = goalkeeper_u1 - t3_p5_attack
        if penalty5 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty6 = goalkeeper_u1 - t3_p6_attack
        if penalty6 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
            
    elif u2_team == "team 4":
        penalty1 = goalkeeper_u1 - t4_p1_attack
        if penalty1 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty2 = goalkeeper_u1 - t4_p2_attack
        if penalty2 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty3 = goalkeeper_u1 - t4_p3_attack
        if penalty3 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty4 = goalkeeper_u1 - t4_p4_attack
        if penalty4 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty5 = goalkeeper_u1 - t4_p5_attack
        if penalty5 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1
        penalty6 = goalkeeper_u1 - t4_p6_attack
        if penalty6 < 0:
            penalty_u2_team += 1
        else:
            penalty_saved_u1 += 1

    if u1_team == "team 1":
        penalty7 = goalkeeper_u2 - t1_p1_attack
        if penalty7 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty8 = goalkeeper_u2 - t1_p2_attack
        if penalty8 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty9 = goalkeeper_u2 - t1_p3_attack
        if penalty9 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty10 = goalkeeper_u2 - t1_p4_attack
        if penalty10 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty11 = goalkeeper_u2 - t1_p5_attack
        if penalty11 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty12 = goalkeeper_u2 - t1_p6_attack
        if penalty12 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u1 += 1
            
    elif u1_team == "team 2":
        penalty7 = goalkeeper_u2 - t2_p1_attack
        if penalty7 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty8 = goalkeeper_u2 - t2_p2_attack
        if penalty8 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty9 = goalkeeper_u2 - t2_p3_attack
        if penalty9 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty10 = goalkeeper_u2 - t2_p4_attack
        if penalty10 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty11 = goalkeeper_u2 - t2_p5_attack
        if penalty11 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty12 = goalkeeper_u2 - t2_p6_attack
        if penalty12 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
            
    elif u1_team == "team 3":
        penalty7 = goalkeeper_u2 - t3_p1_attack
        if penalty7 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty8 = goalkeeper_u2 - t3_p2_attack
        if penalty8 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty9 = goalkeeper_u2 - t3_p3_attack
        if penalty9 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty10 = goalkeeper_u2 - t3_p4_attack
        if penalty10 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty11 = goalkeeper_u2 - t3_p5_attack
        if penalty11 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty12 = goalkeeper_u2 - t3_p6_attack
        if penalty12 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
            
    elif u1_team == "team 4":
        penalty7 = goalkeeper_u2 - t4_p1_attack
        if penalty7 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty8 = goalkeeper_u2 - t4_p2_attack
        if penalty8 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty9 = goalkeeper_u2 - t4_p3_attack
        if penalty9 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1
        penalty10 = goalkeeper_u2 - t4_p4_attack
        if penalty10 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u1 += 1
        penalty11 = goalkeeper_u2 - t4_p5_attack
        if penalty11 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u1 += 1
        penalty12 = goalkeeper_u2 - t4_p6_attack
        if penalty12 < 0:
            penalty_u1_team += 1
        else:
            penalty_saved_u2 += 1

    if penalty_u1_team > penalty_saved_u2:
        print("User 1 is the winner.")
    elif penalty_u2_team > penalty_saved_u2:
        print("User 2 is the winner.")
    else:
        print("It is a tie")


def menu():
    print("***** Welcome to the two player hockey game. ***** \n")
    print("Option 1 : Create the teams.")
    print("Option 2 : Play hockey.")
    print("Option 3 : Exit.\n")
    repeat = "Yes"
    while repeat != "No":
        option = int(input("Please choose an option."))
        if option == 1:
            team_1_details()
            team_2_details()
            team_3_details()
            team_4_details()
            repeat = "Yes"
        elif option == 2:
            game()
            repeat = "Yes"
        elif option == 3:
            print("\nPlease play again soon.")
            repeat = "No"
        else:
            print("\n Incorrect input: This is not an option that is available.\n")
menu()
            
