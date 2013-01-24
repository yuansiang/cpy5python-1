# Filename: q6_find_ascii_char.py
# Author: Justin Leow
# Created: 24/1/2013
# Modified: 24/1/2013
# Description: receives an ASCII code (an integer between 0 and 127) and displays its character.

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
    
    #convert ascii to char
    myOutput = ""
    
    for w in userInput:
        myOutput += str(ord(w)) + "; "
        
    #output
    print(myOutput)
        
