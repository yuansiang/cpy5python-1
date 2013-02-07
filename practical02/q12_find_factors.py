# Filename: q12_find_factors.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: a program that reads an integer and displays all its smallest factors.

#input functions
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

# main

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    userNum = newInt("Enter Integer: ")
    num = userNum
    
    #initialize array which stores all factors
    factorsArr = []
    
    completed = False
    divisor = 2
    
    #test divide
    while(num>=divisor):
        if(num%divisor==0):
            factorsArr.append(divisor)
            num = num / divisor
        else:
            divisor = divisor + 1
    
    #output
    print(factorsArr)
    
