# Filename: compute_bmi.py
# Author: Justin Leow
# Created: 21/1/2013
# Modified: 22/1/2013
# Description: Program to get user weight and height and calculate body mass

# main

while(True):

# get user mass and weight input
    mass = input(["Input mass / kg, or type 'quit'"])
    if(mass=="quit"):
        quit()
    mass=float(mass)
    height = float(input(["input height / cm or m"]))
    if(height>100):
        height/=100 

# calculate bmi
    bmi = mass/(height**2)

#display result
    print("Your BMI is {0:.2f}".format(bmi))
    if(bmi>27/5):
        print("High Risk!")
    elif(bmi>23):
        print("Moderate Risk")
    elif(bmi>18.5):
        print("Low risk. You are healthy :)")
    else:
        print("Risk of nutritional deficiency diseases and osteoporosis. Yoo gon ded!1!")

    print("\n")
