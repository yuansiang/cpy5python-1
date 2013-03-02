# Filename: q7_display_matrix.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays an n by n matrix, with elements generated randomly between 0 and 1

##Input a positive integer: 3
##1 0 1 
##0 1 1 
##0 1 1 
##
##Input a positive integer: 10
##1 1 0 1 0 1 1 0 0 1 
##0 1 1 0 1 0 1 1 0 0 
##0 1 0 1 0 1 0 0 1 0 
##0 1 0 0 1 1 0 1 0 1 
##1 0 1 1 0 0 1 1 0 1 
##0 0 1 1 1 0 1 1 0 1 
##0 1 0 1 1 1 0 0 0 1 
##0 0 1 0 0 0 0 0 0 0 
##1 1 1 0 1 1 0 1 1 1 
##1 0 1 0 1 1 0 0 0 1 

import random

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 3")
        return 3
    tempInput = int(tempInput)
    if(tempInput < 0):
        print("Input is not positive. Utilizing default value of 3")
        return 3
    else:
        return int(tempInput)

# main

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    n = newInt("Input a positive integer: ")
    
    for i in range(n):
        printRow = ""
        for j in range(n):
            printRow += str(random.randint(0,1)) + " "
        print(printRow)
        
    print("")