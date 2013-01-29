# Filename: q02_triangle.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Write a program that reads three edges for a triangle and determines whether the input is valid.
#              The input is valid if the sum of any two edges is greater than the third edge.
#              The program will compute the perimeter of the triangle if the input is valid. Otherwise, display that the input is invalid.

def newFloat(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        float(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return 10
    else:
        tempInput = float(tempInput)
        return tempInput

# main

print("\ntype 'quit' to quit program at anytime.\n")

tri=[0,0,0]

while(True):

    #get user input
    tri[0] = newFloat("Enter side 1: ")
    tri[1] = newFloat("Enter side 2: ")
    tri[2] = newFloat("Enter side 3: ")
    
    
    #calculate
    tri.sort()
    if(tri[0]+tri[1]<=tri[2]):
        print("Invalid triangle!\n")
    else:
        print("Perimeter = "+str(tri[0]+tri[1]+tri[2])+"\n")
