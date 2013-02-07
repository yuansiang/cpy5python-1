# Filename: q10_find_largest.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Use a while loop to find the largest integer n such that n3 is less than 12,000.

# main

n=0

while(n**3<12000):
    n = n+1
    
print(n-1)