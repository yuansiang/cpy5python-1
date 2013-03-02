# Filename: q8_find_uppercase.py
# Author: Justin Leow
# Created: 25/2/2013
# Modified: 25/2/2013
# Description: Returns number of uppercase letters in a string

##Enter a string: Good MorninG!
##3
##Enter a string: I LOVE cake and all KINDS of sweet stuff!
##10

#complementary function which returns 1 if input is uppercase
def isUppercase(foo):
    if ord(foo[0])>=65 and ord(foo[0])<=90:
        return 1
    return 0

#main recursive function
def find_num_uppercase(str):
    if(len(str)==1):
        return isUppercase(str[0])
    else:
        return isUppercase(str[0])+find_num_uppercase(str[1:])
#main
while(True):
    bar = input("Enter a string: ")
    if(bar=="quit"):
        quit()
    print(find_num_uppercase(bar))