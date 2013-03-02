# Filename: q3_find_gcd.py
# Author: Justin Leow
# Created: 22/2/2013
# Modified: 22/2/2013
# Description: Uses a recursive function to compute gcd

##8
##5

def gcd(m,n):
    if(m%n==0):
        return n
    else:
        return gcd(n,m%n)
    
print(gcd(24,16))
print(gcd(255,25))