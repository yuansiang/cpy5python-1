# Filename: q05_find_month_days.py 
# Author: Justin Leow
# Created: 29/1/2013
# Modified: 29/1/2013
# Description: a program that prompts the user to enter the month and year, and displays the number of days in the month. 


def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 1996")
        return 1996
    else:
        tempInput = int(tempInput)
        return tempInput

def checkLeap(year):
    if(year%4==0):
        return "Leap"
    else:
        return "Non-Leap"

def checkDays(month,year):
    if(month%2==1):
        return 31
    elif(month==2):
        if(checkLeap(year) == "Leap"):
            return 29
        else:
            return 28
    else:
        return 30

# main

print("\ntype 'quit' to quit program at anytime.\n")

monthsArr = ["January","February","March","April","May","June","July","August","September","October","November","December",]

while(True):

    #get user input
    month = newInt("Enter month: ")
    year = newInt("Enter year: ")
    
    #output
    print(monthsArr[month-1]+" has "+str(checkDays(month,year))+" days.\n")
    
    