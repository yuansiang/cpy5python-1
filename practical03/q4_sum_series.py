# Filename: q4_sum_series.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays a pattern

# main

def term(n):
    return n/(n+1)

def returnSumSeries(n):
    sum = 0
    for i in range(n+1):
        sum = sum + term(i)
    return sum

# main

print("i     m(i)")

for i in range(1,21):
    print ("{0:<5}".format(str(i)),"{0:<.4f}".format(returnSumSeries(i)))