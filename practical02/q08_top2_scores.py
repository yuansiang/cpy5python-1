# Filename: q08_top2_scores.py
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: prompts the user to enter the number of students and each student's name and score,
#              and finally displays the student with the highest score and the student with the second-highest score.

#input functions
def newFloat(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        float(tempInput)
    except:
        print("Input is not a number. Utilizing default value of 75")
        return 75
    else:
        tempInput = float(tempInput)
        return tempInput

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 3")
        return 3
    else:
        tempInput = int(tempInput)
        if(tempInput<=2):
            print("A class must consist of three or more students.")
            return 3
        else:
            return tempInput
    
def newString(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    elif(tempInput=="egg"):
        tempInput = "Tan Di Sheng the strong black woman who don't need no man"
    return tempInput
    
# main

print("\ntype 'quit' to quit program at anytime.\n")

while(True):

    studentNames=[]
    studentScores=[]

    #get user input
    numStudents = newInt("Enter number of students in class: ")
    for i in range(numStudents):
        studentNames.append(newString("Input name of student "+str(i+1)+": "))
        studentScores.append(newFloat("Input "+studentNames[i]+"'s score: "))
    #print(studentNames,studentScores)
    
    #calculate id of students with second highest scores
    if(studentScores[1]>studentScores[0]):
        highestStudent = [studentScores[1],studentNames[1]]
        secondStudent = [studentScores[0],studentNames[0]]
    else:
        highestStudent = [studentScores[0],studentNames[0]]
        secondStudent = [studentScores[1],studentNames[1]]
    
    for i in range(numStudents):
        if(studentScores[i]>highestStudent[0]):
            secondStudent = highestStudent
            highestStudent = [studentScores[i],studentNames[i]]

    #output
    print("\nThe student with the highest score is {0} with a score of {1:.1f}".format(highestStudent[1],highestStudent[0]))
    print("The student with the second highest score is {0} with a score of {1:.1f} \n".format(secondStudent[1],secondStudent[0]))
    