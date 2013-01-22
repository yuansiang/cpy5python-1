# Filename: q2_calc_cylinder_volume.py
# Author: Justin Leow
# Created: 22/1/2013
# Modified: 22/1/2013
# Description: Program which processes the radius and length of a cylinder and
#              outputs the volume of the calculated cylinder.

from math import pi


# main

while(True):

    #get user input radius
    rInput = input(["Input radius of cylinder in units, or 'quit' to quit"])
    if(rInput=="quit"):
        quit()
    try:
        float(rInput)
    except:
        print("Please input a number \n")
        continue
    radius=float(rInput)

    #get user input length
    lInput=input(["Input length of cylinder in units"])
    try:
        float(lInput)
    except:
        print("Please input a number \n")
        continue
    length=float(lInput)

    #calculate volume
    area = radius**2 * pi
    volume = area * length

    #output volume
    print("The volume of the cylinder is: {0:.2f}".format(volume) + "\n")
        
