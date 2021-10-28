#!/usr/bin/bash

# David Kumar
# 09/16/2021

import os
import socket
import netifaces
import subprocess


# Gives the user options to input
def user_options():
    # Neatly gives options
    print("Welcome, here we will test various network capabilities....\n")
    print("Please select the option told\n")
    print("1. Test Default Gateway")
    print("2. Test remote IP address")
    print("3. Test DNS resoultion")
    print("4. Display default gateway")
    print("5. Exit program\n")


# Tests if the default gateway is reachable
def test_default(default_gateway):

    # Creates the ping command
    process = subprocess.Popen(['ping','-c' ,'1', str(default_gateway)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # With 4 packets
    stdout, stderr = process.communicate()
    returncode = process.returncode


    if returncode == 0:							# Returns based on result
        return("\nPing sucessful")

    else:
        return("\nPing Unsucessful")

    

# Tests if the device can ping a remote device
def test_remote_host(remote_ip):

     # Creates the ping command
    process = subprocess.Popen(['ping','-c' ,'1', str(remote_ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # With 4 packets
    stdout, stderr = process.communicate()
    returncode = process.returncode

    if returncode == 0:							# Returns based on result
        return("\nPing sucessful")

    else:
        return("\nPing Unsucessful")


# Tests if the DNS is able to resolve a domain name
def test_dns(google_ip):

    print("Testing name resoultion of 'www.google.com' .....\n")

     # Creates the ping command
    process = subprocess.Popen(['ping','-c' ,'1', str(google_ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # With 4 packets
    stdout, stderr = process.communicate()
    returncode = process.returncode

    if returncode == 0:							# Returns based on result
        return("\nPing sucessful")

    else:
        return("\nPing Unsucessful")


# Tests if the ip address inputed is correct
def test_ip(ip_address):

    ip_address_split = ip_address.split('.')
    if len(ip_address_split) != 4:							# Analyzes the ip address entered
        return False
    for i in ip_address_split:
        if not i.isdigit():
            return False
        v = int(i)
        if v < 0 or v > 255:
            return False
    return True


if __name__ == '__main__':

    hostname = socket.gethostname()							# Gets information about the network
    local_ip = socket.gethostbyname(hostname)
    network_gateways = netifaces.gateways()
    default_gateway = network_gateways['default'][netifaces.AF_INET][0]
    rit_dns = "129.21.3.17"
    google_ip = "142.251.32.100"

    os.system('clear')

    while True:

        user_options()

        user_input = input("Which option would you like to run: ")

        if(user_input == "1"): 								# Sees the options and runs the functions
            os.system('clear')
            print("Testing.....\n")
            print(test_default(default_gateway))
            input("\nPlase report this to the technican and press enter to leave ")
            os.system('clear')

        elif(user_input == "2"):
            ip_input = input("\nPlease enter an IP address: ")
            # Makes sure that the ip address entered is in a correct format
            if (test_ip(ip_input) == False):
                os.system('clear')
                print(
                    "\nIncorrect format, please enter an ip address in the format of #.#.#.#")
                input("\nPlase report this to the technican and press enter to leave ")
                os.system('clear')
            else:
                os.system('clear')
                print("\nTesting.....\n")
                print(test_remote_host(ip_input))
                input("\nPlease report this to the technican and press enter to leave ")
                os.system('clear')

        elif(user_input == "3"):
            os.system('clear')
            print(test_dns(google_ip))
            input("\nPlase report this to the technican and press enter to leave ")
            os.system('clear')

        elif(user_input == "5"):							   # Makes sure the user wants to actually quit
            os.system('clear')
            exit_input = input(
                "\nYou are now exiting the program, are you sure y/n: ")
            if(exit_input == "y"):
                print("Now exiting.....")
                break
            elif(exit_input == "n"):
                print("Returning to program....")
                os.system('clear')
                continue
            else:
                os.system('clear')
                print("Please enter 'y' or 'n' ")
                input("\nPlase report this to the technican and press enter to leave ")
                os.system('clear')
                
        elif(user_input == "4"):
            os.system("clear")
            print("Your default gateway is " + str(default_gateway))
            input("\nPlase report this to the technican and press enter to leave ")
            os.system('clear')

        else:										        # Asks for correct input
            os.system('clear')
            print("Incorrect input...")
            input("Press enter to return......")
            os.system('clear')
