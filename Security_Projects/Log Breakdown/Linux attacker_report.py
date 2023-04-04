#!/usr/bin/env/python3

# David Kumar
# 11/1/2021


import os
import re
from typing import Counter
from geoip import geolite2 


def find_location(ip_address):                                          # Finds geolocation given Ip

    country = str(geolite2.lookup(ip_address))                          # Finds the geolocation
    listed_info= list(country.split("'"))                               # Seperates the different info

    return listed_info[3]                                               # Returns the country info


def get_frequency(data_list):                                           # Gets the frequency of IP

    counts = Counter(data_list)                                         # Creates a dictionary with its frequency
    sorted_counts_tuples = sorted(counts.items(), key= lambda kv: kv[1])# Sorts the dictionary by its frequency 
    sorted_counts_dict= dict(sorted_counts_tuples)                      # Turns the tuples back to dictionary
    return sorted_counts_dict                                           # Returns the sorted dictionary 

    

def read_file(log_file):                                                # Reads .log file
    
    regex_string = "Failed password for root from"                      # Target string to find

    data_list = []                                                      # Creates an empty list to store info

    with open(log_file, 'r') as f:                                      # Process reads the file
        lines =f.readlines()
        for string in lines:
            if re.search(regex_string, string):                         # Searches for target key
                split = string.split(" ")

                ip = split[10]
                data_list.append(ip)                                    # If the target is found, stores the IP
        
    return data_list                                                    # Returns the list of IPs


if __name__ == '__main__':

    os.system("clear")                                                  # Clears screen

    print("Attacker Report: " + os.popen("date '+%b %d %Y'  ").read())  # Prints todays date in format

    log_file= "./syslog.log"                                            # Stores log file in pwd

    print("COUNT\t\t IP ADDRESS\t\t COUNTRY")                           # Clear format for user

    data= read_file(log_file)                                           # File is read and returns list of IPs

    frequency= get_frequency(data)                                      # Takes list and returns a dictionary of IP frequency 

    sorted_data_list = sorted(data, key = data.count)                   # Sorts the list by the frequency 
        
    non_duplicate_data= []                                              # Empty list to store unqiue IPs
    for i in sorted_data_list:                              
        if i not in non_duplicate_data:
            non_duplicate_data.append(i)                                # Removes duplicates and inputs unique IPs
                                                                        # Attempted using sets but messed with sorting

    for i in range(len(non_duplicate_data)):                            # Prints the frequency, IP and country in clear format for each entry
        print(frequency.get((non_duplicate_data[i])), "\t\t "+ non_duplicate_data[i] + "\t\t " + find_location(non_duplicate_data[i]))
    
    print("\n")
