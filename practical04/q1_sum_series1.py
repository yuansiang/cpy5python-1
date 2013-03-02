# Filename: q1_sum_series1.py
# Author: Justin Leow
# Created: 22/2/2013
# Modified: 22/2/2013
# Description: Uses a recursive function to compute m(i) = 1 + 1/2 + 1/3 + ... 1/i

##Insert i: 3
##1.8333333333333333 
##
##Insert i: 10
##2.9289682539682538 

#custom input function
def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return 10
    tempInput = int(tempInput)
    if(tempInput < 0):
        print("Input is not positive. Utilizing default value of 10")
        return 10
    else:
        return tempInput
    
#main recursive function
def m(i):
    if(i==1):
        return 1
    else:
        return float(1/i + m(i-1))

#main
print("\ntype 'quit' to quit program at anytime.\n")

while(True):
    foo = newInt("Insert i: ")
    print(m(foo),"\n")