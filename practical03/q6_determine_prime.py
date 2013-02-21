# Filename: q6_determine_prime.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays prime numbers from 1<n<1000

from math import *

def is_prime(n):
    if(n<2):
        return False
    for k in range(2,int(sqrt(n)+1)):
        if(n%k==0):
            return False
    return True

myList = []

for i in range(1001):
    if(is_prime(i)):
        myList.append(i)

listLength = len(myList)
rows = ceil(listLength / 10)
for j in range(0,rows):
    printRow = ""
    for k in range(10):
        printRow += "{0:<5} ".format(str(myList[j*10+k]))
    print(printRow)