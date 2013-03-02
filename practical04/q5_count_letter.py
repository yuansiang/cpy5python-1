# Filename: q5_count_letter.py
# Author: Justin Leow
# Created: 22/2/2013
# Modified: 22/2/2013
# Description: Counts the number of occurances of a character in a string

##Insert string to search through: my elephant loves to jump through elephant hoops
##Insert character to search for: e
##5 


def newString(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    return tempInput

def newChar(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    elif(len(tempInput)!=1):
        print("Input isn't a single character! Searching for i instead...")
        return "i"
    else:
        return tempInput
    
#main recursion function
def count_letter(str,ch):
    if(len(str)==1):
        return(str==ch)
    else:
        return(str[0]==ch)+count_letter(str[1:],ch)

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    str = newString("Insert string to search through: ")
    ch = newChar("Insert character to search for: ")
    
    #main
    
    
    #output
    print(count_letter(str,ch),"\n")