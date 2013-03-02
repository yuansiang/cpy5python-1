# Filename: q5_compute_series.py
# Author: Justin Leow
# Created: 21/2/2013
# Modified: 21/2/2013
# Description: displays a pattern

##i     m(i)
##1     2.66666666667
##3     2.89523809524
##5     2.97604617605
##7     3.01707181707
##9     3.04183961893
##11    3.05840276593
##13    3.07025461778
##15    3.07915339420
##17    3.08607980112
##19    3.09162380667

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