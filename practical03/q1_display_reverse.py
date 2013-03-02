# Filename: q1_display_reverse.py
# Author: Justin Leow
# Created: 19/2/2013
# Modified: 22/2/2013
# Description: Displays an integer in reverse order

##Input a positive integer: 5627631
##1367265
##Input a positive integer: nope
##Input is not an integer. Utilizing default value of 6593
##3956
##Input a positive integer: quit

def newString(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 6593")
        return 6593
    tempInput = int(tempInput)
    if(tempInput < 0):
        print("Input is not positive. Utilizing default value of 6593")
        return 6593
    else:
        return tempInput

# main

while(True):

    #get user input
    myNumber = str(newString("Input a positive integer: "))
    
    print (int(myNumber[::-1]))
        
