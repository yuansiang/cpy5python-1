# Filename: q03_determine_grade.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: A program that prompts the user to enter a score between 0 and 100 inclusive, then gives him his grade.

def newFloat(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        float(tempInput)
    except:
        print("Input is not a number. Utilizing default value of 10")
        return 10
    else:
        tempInput = float(tempInput)
        if(0<=tempInput<=100):
            return tempInput
        else:
            print("Invalid! Score must be within 0 - 100.")

# main

print("\ntype 'quit' to quit program at anytime.\n")

looping = True

while(True):

    #get user input
    userInput = newFloat("Enter score: ")
    
    grades = ["EXCELLENT FULL COMBO SSS","A","B","C","D","E","S","U"]
    gradeScore = [100,70,60,55,50,45,35,0]
    gradeArr = [grades,gradeScore]
    
    if(userInput==gradeArr[1][0]):
        print(gradeArr[0][0]+"\n")
    else:
        for i in range(1,len(gradeScore)):
            if(gradeArr[1][i-1]>userInput>=gradeArr[1][i]):
                print(gradeArr[0][i]+"\n")