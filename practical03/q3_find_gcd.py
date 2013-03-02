# Filename: q3_find_gcd.py
# Author: Justin Leow
# Created: 19/2/2013
# Modified: 19/2/2013
# Description: returns the greatest common divisor between two positive integers

##The greatest common divisor of 16 and 24 is 8
##The greatest common divisor of 255 and 25 is 5

# main

def gcd(n1,n2):
    
    if(n1>n2):
        d = n2
    else:
        d = n1
    
    gcdfound = False
    while(gcdfound==False):
        if(n1%d==0 and n2%d==0):
            gcdfound = True
        else:
            d = d-1
    
    #output
    print("The greatest common divisor of {0} and {1} is {2}".format(n1,n2,d))
    
gcd(16,24)
gcd(255,25)