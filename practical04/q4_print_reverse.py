# Filename: q4_print_reverse.py
# Author: Justin Leow
# Created: 22/2/2013
# Modified: 22/2/2013
# Description: Displays an integer in reverse order

##Input a positive integer: 12345
##54321
##Input a positive integer: 72561721516
##61512716527
##Input a positive integer: k
##Input is not an integer. Utilizing default value of 6593
##3956

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 6593")
        return 6593
    tempInput = int(tempInput)
    if(tempInput < 0):
        print("Input is not positive. Utilizing default value of 6593")
        return 6593
    else:
        return tempInput

def reverse_int(n):
    if(n<10):
        return str(n)
    else:
        return str(n%10) + reverse_int(n//10)


# main
print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    #get user input
    myNumber = newInt("Input a positive integer: ")
    
    print(reverse_int(myNumber))
