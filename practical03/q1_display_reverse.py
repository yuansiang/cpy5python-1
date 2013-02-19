# Filename: q1_display_reverse.py
# Author: Justin Leow
# Created: 19/2/2013
# Modified: 19/2/2013
# Description: Displays an integer in reverse order

def newString(inputString):
    tempInput = input([inputString + "; or 'quit' to quit program"])
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 6593")
        return "6593"
    return tempInput

# main

while(True):

    #get user input
    myNumber = str(newString("Input a positive integer"))
    
    print (myNumber[::-1])
        
