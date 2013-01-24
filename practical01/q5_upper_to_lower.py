# Filename: q5_upper_to_lower.py
# Author: Justin Leow
# Created: 24/1/2013
# Modified: 24/1/2013
# Description: converts an uppercase letter from standard input to a lowercase letter by making use of its ASCII value

def newString(inputString):
    tempInput = input([inputString + "; or 'quit' to quit program"])
    if(tempInput=="quit"):
        quit()
    elif(tempInput=="egg"):
        tempInput = "Tan Di Sheng is a strong black woman who don't need no man"
    return tempInput

# main

while(True):

    #get user input
    userInput = newString("Input an English sentence.")
    
    #Shortcut
    #myOutput = userInput.lower()
    
    #convert uppercase characters in string into lower case
    myOutput = ""
    
    for w in userInput:
        currentascii = ord(w)
        #print(currentascii,chr(currentascii),i,myOutput[i])
        
        if(65<=currentascii<=90):
            myOutput+=chr(currentascii+32)
        else:
            myOutput+=chr(currentascii)
        

    #output
    print(myOutput)
        
