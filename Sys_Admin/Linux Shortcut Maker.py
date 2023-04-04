#!/usr/bin/bash

# David Kumar
# 10/21/2021

import os


def user_options():

    print("\t\t*************************************************")
    print("\t\t*************** Shortcut Creator ****************")
    print("\t\t*************************************************")

    print("\n\nEnter Selection:")
    print("\t\t1 - Create a shortcut in your home directory.")
    print("\t\t2 - Remove a shortcut from your home directory.")
    print("\t\t3 - Run shortcut report. ")

def check_file_existance(file_input):

    check = os.system("find /home -name " + file_input)

    if "/home" in check:
        return check
    else:
        return 0



    return

def create_shortcut():

    print("Searching for file....")

    file_input = input("Please enter the file name to create a shortcut:\t")
    file_exists = check_file_existance(file_input)

    if file_exists == 0:
        print("file does not exist")
    else:
        create_option= input("Found " + file_exists + ". Select Y/y to create the shortcut ")

    if create_option == "y" or create_option == "Y":
        
        print("Blob")

    elif create_option == "N" or create_option == "n":
        print("Returning to menu...")
    
    else:

        print("bob2")



if __name__ == '__main__':

    while True:

        user_options()
        
        user_input = input("\nPlease enter a number (1-3) or 'Q/q' to quit your program\t") 

        if(user_input == "1"):
            os.system("cls")
            create_shortcut()
            

        elif(user_input == "2"):
            os.system("cls")
            file_input = input("Please enter the shortcut/link to remove:")

        elif(user_input == "3"):
            os.system("cls")
            print("\t\t*************************************************")
            print("\t\t*************** Shortcut Report *****************")
            print("\t\t*************************************************")

            input("\nPlease enter a number (1-3) or 'Q/q' to quit the program.")

        elif(user_input == 'Q' or user_input == 'q'):
            os.system("cls")
            print("Quiting program: returning to shell.")
            print("\nHave a wonderful day!\n")
            break

        else:
            print("Incorrect input....")
            print("\nReturning to main menu......")


    


    