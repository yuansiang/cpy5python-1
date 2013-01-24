# Filename: q4_sum_digits.py
# Author: Justin Leow
# Created: 24/1/2013
# Modified: 24/1/2013
# Description: reads an integer between 0 and 1000 and adds all the digits in the integer.

def newString(inputString):
    tempInput = input([inputString + "; or 'quit' to quit program"])
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not a number. Utilizing default value of 10")
        return "10"
    return tempInput

# main

while(True):

    #get user input
    myNumber = newString("Input a positive integer")
    
    #Get number of characters in the string
    numElements = len(myNumber)
    
    currentNumber = 0
    
    for i in myNumber:
        currentNumber += int(i)

    #output volume
    print("The sum of all the digits in your number is: {0:.0f}! \n".format(currentNumber))
        
