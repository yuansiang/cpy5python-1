# Filename: q11_find_gcd.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Find the greatest common divisor between two numbers

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
    n1 = newInt("Enter First Number: ")
    n2 = newInt("Enter Second Number: ")
    
    #calculate
    if(n1>n2):
        d = n2
    else:
        d = n1
    
    gcdfound = False
    while(gcdfound==False):
        if(n1%d==0 and n2%d==0):
            gcdfound = True
        else:
            d = d-1
    
    #output
    print("The greatest common divisor is : "+str(d))
    
