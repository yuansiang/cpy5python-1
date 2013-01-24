# Filename: q7_generate_payroll.py
# Author: Justin Leow
# Created: 24/1/2013
# Modified: 24/1/2013
# Description: prints a payroll statement. 

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
        return tempInput

def newInt(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    try:
        int(tempInput)
    except:
        print("Input is not an integer. Utilizing default value of 10")
        return 10
    else:
        tempInput = int(tempInput)
        return tempInput

def newString(inputString):
    tempInput = input(inputString)
    if(tempInput=="quit"):
        quit()
    elif(tempInput=="egg"):
        tempInput = "Tan Di Sheng is a strong black woman who don't need no man"
        
    return tempInput

# main

while(True):
    
    #Prompt/remind user of quit function
    print("enter 'quit' at any time to quit program \n")
    
    #get user input
    name = newString("Enter name: ")
    hours = newInt("Enter number of hours worked weekly: ")
    payrate = newFloat("Enter hourly pay rate: ")
    cpfRate = newFloat("Enter CPF contribution rate (%): ")
    
    #calculate
    grossPay = payrate*hours
    cpfContribution = cpfRate/100*grossPay
    netPay = grossPay - cpfContribution
    
    

    #output
    #print("Payroll statement for "+name+"\n Number of hours worked in week: "+hours+"\n Hourly pay rate: ${0:.2f} \n Gross pay = ${1:.2f} \n CPF Contribution at ".format(payrate,grossPay) + cpfRate+"% = ${0:.2f} \n \n Net pay = ${1:.2f}".format(cpfContribution,netPay))
    print("\nPayroll statement for "+name)   
    print("Number of hours worked in week = "+str(hours))
    print("Hourly pay rate = ${0:.2f}".format(payrate))
    print("Gross pay = ${0:.2f}".format(grossPay))
    print("CPF contribution at "+str(cpfRate)+"% = ${0:.2f} \n".format(cpfContribution))
    print("Net pay = ${0:.2f} \n".format(netPay))
