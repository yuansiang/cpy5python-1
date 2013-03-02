# Filename: q6_sum_digits.py
# Author: Justin Leow
# Created: 22/2/2013
# Modified: 22/2/2013
# Description: Sums the digits in an integer

##Insert positive integer to sum digits of: 234
##9 


#custom input function
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
    
    
#main recursive function
def sum_digits(n):
    if(n < 10):
        return n
    else:
        return sum_digits(n//10) + n%10

#main
print("\ntype 'quit' to quit program at anytime.\n")

while(True):
    foo = newInt("Insert positive integer to sum digits of: ")
    print(sum_digits(foo),"\n")