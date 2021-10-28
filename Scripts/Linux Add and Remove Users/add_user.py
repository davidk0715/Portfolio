#!/bin/bash

#David Kumar
#10/06/2021

import os 
import csv
import string

PASSWORD = "password"                                            # Default Password

def reading_csv(filename):                                       # Reads the CSV File
    
    fields = []
    rows = []

    with open(filename, 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        
        fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)
    
    return rows

def add_users(user_list):                                       # Adds user to local group

    current_added_users = list()
    count=1

    for i in range(len(user_info)):                             # Goes through the execl

        if(i == len(user_info)):
            break
        
        else:

            id = str(user_list[i][0])                           # Assigns feild to variables
            last_name= str(user_list[i][1])
            first_name= str(user_list[i][2])
            first_name_letter = str(user_list[i][2][:1])
            office = str(user_list[i][3])
            phone = str(user_list[i][4])
            department = str(user_list[i][5])
            group = str(user_list[i][6])
           
        
            username= first_name_letter + last_name            
            for i in range(len(username) -1):                   # Deals with special characters
                if username[i] == "'":
                   username= username.replace("'","")
                else:
                    continue
                
            lowered_username = username.lower()                 # lowers username

            home_directory = "/home/"+department+"/"+lowered_username    # makes the home directory

            if(lowered_username in current_added_users):
                lowered_username+= str(count)
                current_added_users.append(lowered_username)
            else:
                current_added_users.append(lowered_username)

            if group == "office":
                shell = "/bin/csh"
            else:
                shell = "/bin/bash"
            
            if(id != "" and first_name != "" and last_name != "" and office != "" and phone != "" and department != "" and group != ""):                # If all is correct, it creates the users
                print("Processing employee ID " + id + ".\t"+ lowered_username + " added to system\n")
                os.system("sudo useradd " + lowered_username +" -d " + home_directory +" -s "+ shell +" -g " + group + " -p " + PASSWORD )              # Makes user with default password
                os.system("sudo passwd --expire " + lowered_username)                                                                                   # expires the password

            elif (id == "" or first_name == "" or last_name == "" or office == ""  or group == ""):                                                     # Detects missing info
                print("Cannot process ID " + id + ".\tInsufficient data.\n")

            elif(group != "pubsafety" or group != "office" or group== ""):                                                                              # Detects incorrect groups
                print("Cannot process ID " + id + ".\tNot a valid group\n")


if __name__ == '__main__':

    os.system("clear")                                                                                                                                  # Clears cmd line
    os.system("sudo groupadd -f office")                                                                                                                # Adds group
    os.system("sudo groupadd -f pubsafety")                                                                                                             # Adds group
    os.chdir("/home")                                                                                                                                   # Goes to home 
    os.system("sudo mkdir ceo")                                                                                                                         # Makes folders
    os.system("sudo mkdir security")
    os.chdir("/home/student/Downloads")
    print("Adding new users to the system.")
    print("Please Note: The default password for new users is password")
    print("For testing purposes. Change the password 1$4pizz@.\n")

    user_info = reading_csv("linux_users.csv")                                                                                                          # Reads the file

    add_users(user_info)                                                                                                                                # Adds users 
