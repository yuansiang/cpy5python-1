# Filename: q4_sum_series.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays a pattern

##i     m(i)
##1     0.5000
##2     1.1667
##3     1.9167
##4     2.7167
##5     3.5500
##6     4.4071
##7     5.2821
##8     6.1710
##9     7.0710
##10    7.9801
##11    8.8968
##12    9.8199
##13    10.7484
##14    11.6818
##15    12.6193
##16    13.5604
##17    14.5049
##18    15.4523
##19    16.4023
##20    17.3546

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