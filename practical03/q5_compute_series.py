# Filename: q5_compute_series.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays a pattern

# main

def term(n):
    return 4*(1/(2*n-1)-1/(2*n+1))

def returnSumSeries(n):
    sum = 0
    for i in range(1,n+2,2):
        sum = sum + term(i)
    return sum

# main

print("i     m(i)")

for i in range(1,11):
    currentTerm = i*2-1
    print("{0:<5}".format(str(currentTerm)),"{0:<.11f}".format(returnSumSeries(currentTerm)))
    #print ("{0:<5}".format(str(i)),"{0:<.11f}".format(returnSumSeries(i)))