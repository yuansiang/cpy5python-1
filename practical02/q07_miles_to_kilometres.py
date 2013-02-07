# Filename: q07_miles_to_kilometres.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Write a program that displays two tables of x miles to kilometres, and kilometres to miles where 1<x<10

def milesToKm(input):
    return input*1.609
def kmToMiles(input):
    return input*(1/1.609)

# main

print("\ntype 'quit' to quit program at anytime.\n")

print("Miles Kilometers Kilometres Miles")

w=20

for i in range(1,11):
    print("{0:<6}{1:<11.3f}{2:<11}{3:.3f}".format(i,milesToKm(i),w,kmToMiles(w)))
    w+=5