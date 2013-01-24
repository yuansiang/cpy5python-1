# Filename: q3_miles_to_kilometre.py
# Author: Justin Leow
# Created: 22/1/2013
# Modified: 22/1/2013
# Description: reads a number in miles, converts it to kilometres, and displays the result. One mile is 1.60934 kilometres. Display your answer correct to 3 decimal places.

def newFloat(inputString):
    tempInput = input([inputString + "; or 'quit' to quit program"])
    if(tempInput=="quit"):
        quit()
    try:
        float(tempInput)
    except:
        print("Input is not a number. Utilizing default value of 10")
        return 10
    else:
        tempInput = float(tempInput)
        return tempInput

# main

while(True):

    #get user input in kilometres
    kilometres = newFloat("Input distance to convert in kilometres")
    
    #calculate
    miles = kilometres * 1.60934

    #output volume
    print("{0:.2f}".format(miles) + "miles \n")
        
