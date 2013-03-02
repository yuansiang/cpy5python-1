# Filename: q7_find_largest.py
# Author: Justin Leow
# Created: 25/2/2013
# Modified: 25/2/2013
# Description: Finds largest integer in an array

##Insert num of elements in array: 3
##Input element: 12 
##Input element: 34
##Input element: 2
##34
##
##Insert num of elements in array: 5
##Input element: 1
##Input element: 2
##Input element: 3
##Input element: 78
##Input element: 999
##999

#main recursive function
def find_largest(foo):
    if(len(foo)==2):
        if(foo[0]>foo[1]):
            return foo[0]
        return foo[1]
    else:
        if(foo[0]>foo[1]):
            foo[1]=foo[0]
        return find_largest(foo[1:])
    
#print(find_largest(alist))

#main
while(True):
    alist=[]
    arrayLen = input("Insert num of elements in array: ")
    if(arrayLen=="quit"):
        quit()
    for i in range(int(arrayLen)):
        alist.append(int(input("Input element: ")))
    print(str(find_largest(alist))+"\n")
    