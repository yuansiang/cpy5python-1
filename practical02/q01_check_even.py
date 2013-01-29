# Filename: q01_check_even.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Write a program that reads an integer and checks whether it is even

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return 10
    else:
        tempInput = int(tempInput)
        return tempInput

def checkEven(myInt):
    if(myInt%2):
        return "odd"
    else:
        return "even"

# main

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    userInput = newInt("Enter Number: ")
    
    #output
    print("The number "+str(userInput)+" is an "+str(checkEven(userInput))+" number. \n")
        
