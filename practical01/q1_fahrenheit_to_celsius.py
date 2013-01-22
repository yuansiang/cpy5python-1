# Filename: q1_fahrenheit_to_celsius.py
# Author: Justin Leow
# Created: 22/1/2013
# Modified: 22/1/2013
# Description: Program which converts an input of temperature in farenheit to an
#              output in celcius

# main

while(True):

    #get user input farenheit
    fInput = input(["Input temperature in farenheit, or 'quit' to quit"])
    if(fInput=="quit"):
        quit()
    try:
        float(fInput)
    except:
        print("please input a number")
    else:
        fInput=float(fInput)

        #calculate celcius
        cOutput=(5/9)*(fInput-32)

        #display result
        print("{0:.2f}".format(cOutput)+"\n")
