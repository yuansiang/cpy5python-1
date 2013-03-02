# Filename: q2_display_pattern.py
# Author: Justin Leow
# Created: 19/2/2013
# Modified: 22/2/2013
# Description: Displays a pattern from 1 to n

##Input a positive integer: 10
##                    1
##                  2 1
##                3 2 1
##              4 3 2 1
##            5 4 3 2 1
##          6 5 4 3 2 1
##        7 6 5 4 3 2 1
##      8 7 6 5 4 3 2 1
##    9 8 7 6 5 4 3 2 1
## 10 9 8 7 6 5 4 3 2 1
##Input a positive integer: 3
##     1
##   2 1
## 3 2 1


def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return 10
    tempInput = int(tempInput)
    if(tempInput < 0):
        print("Input is not positive. Utilizing default value of 10")
        return 10
    else:
        return tempInput

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

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    num = newInt("Input a positive integer: ")
    
    displayPattern(num)
