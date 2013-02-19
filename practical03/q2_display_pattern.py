# Filename: q2_display_pattern.py
# Author: Justin Leow
# Created: 19/2/2013
# Modified: 19/2/2013
# Description: Displays a pattern from 1 to n

def newInt(inputString):
    tempInput = input([inputString + "; or 'quit' to quit program"])
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return "10"
    return int(tempInput)

def displayPattern(n):
    myList = []
    #length = n*2
    for j in range(1, n+1):
        myList.append(" " + str(j))
        
    length = len("".join(myList))
    myList=[]
    
    for i in range(1,n+1):
        myList.append(" "+str(i))
        print("{0:>s}".format(("".join(myList[::-1]))).rjust(length))
    
# main

while(True):

    #get user input
    num = newInt("Input a positive integer")
    
    displayPattern(num)
