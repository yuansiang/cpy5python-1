# Filename: q04_determine_leap_year.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Write a program that prompts the user to enter a year and determines whether it is a leap year. 

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 1996")
        return 1996
    else:
        tempInput = int(tempInput)
        return tempInput

def checkLeap(year):
    if(userInput%4==0):
        return "Leap"
    else:
        return "Non-Leap"

# main

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    userInput = newInt("Enter year: ")
    
    #output
    print(checkLeap(userInput))
    
    