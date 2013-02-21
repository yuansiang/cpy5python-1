# Filename: q8_convert_milliseconds.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays an n by n matrix, with elements generated randomly between 0 and 1

import random

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 555550000")
        return 555550000
    return int(tempInput)

# main

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    ms = newInt("Input a positive integer: ")
    
    #calculate from bottom up
    s = int(ms / 1000)
    minutes = int(s / 60)
    h = int(minutes / 60)
    
    s = s % 60
    minutes = minutes % 60
    
    
    print("{0}:{1}:{2}\n".format(h,minutes,s))