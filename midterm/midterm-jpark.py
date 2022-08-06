#!/user/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: Python Scripting Midterm Exam
"""


#print name
print("Name: Gavin Hammer-Perdew")


#dictionaries

password_database = {"Username":"dnedry", "Password":"please"}

command_database = {"reboot":"OK. I will reboot all park systems.",
                    "shutdown":"OK. I will shut down all park systems.",
                    "done":"I hate all this hacker stuff."}


#loop variables

counter = 0 #count authentication failures
white_rabbit_object = 0 #break loop


#loop used to authenticate user

while white_rabbit_object == 0 and counter < 3:

    #get user/pass from user
    input_user = input("Username: ")
    input_password = input("Password: ")

    if input_user == password_database["Username"] and input_password == password_database["Password"]:

        white_rabbit_object = 1 #breaks loop once if statement is complete

        print("Hi Dennis. You're still the best hacker in Jurassic Park.")

        print(f"Please enter one of the following commands: {list(command_database.keys())}")

        #get command from user
        command = input("--> ")

        #evaluate entered command
        if command.lower() == "reboot":
            print(command_database["reboot"])
        elif command.lower() == "shutdown":
            print(command_database["shutdown"])
        elif command.lower() == "done":
            print(command_database["done"])
        else:
            print("The Lysine Contingency has been put into effect.")

    else:

        #if authentication fails, take count and print some unique messages
        counter += 1

        if counter == 3:
            print(f"You didn't say the magic word\n" * 25)

        else:
            print(f"You didn't say the magic word. {counter}")
