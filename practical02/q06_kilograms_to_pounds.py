# Filename: q06_kilograms_to_pounds.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: Write a program that displays a table of x kilos to pounds where 1<x<10

def kiloToPound(input):
    return input*2.2

# main

print("\ntype 'quit' to quit program at anytime.\n")

print("Kilograms Pounds")

for i in range(1,11):
    print("{0:<10}{1:.1f}".format(i,kiloToPound(i)))