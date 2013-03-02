# Filename: q2_sum_series2.py
# Author: Justin Leow
# Created: 22/2/2013
# Modified: 22/2/2013
# Description: Uses a recursive function to compute m(i) = 1/3 + 2/5 + ... + i/(2i+i)

##Insert i: 3
##1.161904761904762
##Insert i: 10
##4.409562711110699

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return 10
    else:
        return int(tempInput)
    
def m(i):
    if(i==1):
        return 1/3
    else:
        return float(i/(2*i + 1) + m(i-1))

#main
print("\ntype 'quit' to quit program at anytime.\n")
    
while(True):
    foo = newInt("Insert i: ")
    print(m(foo))