# Filename: q2_calc_cylinder_volume.py
# Author: Justin Leow
# Created: 22/1/2013
# Modified: 22/1/2013
# Description: Program which processes the radius and length of a cylinder and
#              outputs the volume of the calculated cylinder.

from math import pi

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

    #get user input radius
    radius = newFloat("Input radius of cylinder in units")
    
    #get user input length
    length = newFloat("Input length of cylinder in units")

    #calculate volume
    area = radius**2 * pi
    volume = area * length

    #output volume
    print("The volume of the cylinder is: {0:.2f}".format(volume) + "\n")
        
