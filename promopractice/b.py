def quick_sort(A):
	if len(A) == 0:
		return []

	pivot = A[0]
	less = []
	great = []
	
	for element in A[1:]:
		if element[1] < pivot[1]:
			less.append(element)
		else:
			great.append(element)
			
	less = quick_sort(less)
	great = quick_sort(great)
	return less + [pivot] + great


##main
transfile = open("TRANSACTIONS.dat","r")
infile = open("EMPLOYEE.dat","r")
outfile = open("NEWEMPLOYEE.dat","w")

translist = []

transline = transfile.readline()
while transline != "":
	temptransac = transline[14:].split("E") #interpret all transactions in file and put it in a 2d array
	transac = []
	transac.append(temptransac[0])
	transac.append(int(temptransac[1][0:3]))
	transac.append(temptransac[1][3:])

	translist.append(transac)
	
	transline = transfile.readline()
	
#quicksort
translist = quick_sort(translist)
print(translist)

line = infile.readline()

currTrans = 0
if currTrans < len(translist):
	transType = translist[currTrans][0]
	transID = translist[currTrans][1]
	transDetails = translist[currTrans][2]
	
	transIDString = str(transID)
	if len(transIDString) == 1:
		transIDString = "00" + transIDString
	elif len(transIDString) == 2:
		transIDString = "0" + transIDString
	
	string = "E" + transIDString + transDetails


while line != "":
	
	currID = int(line[1:4])
	print(currID, transID)
		
	while currID > transID and currTrans < len(translist):
		if transType == "A":
			outfile.write(string)
			
			#nextTransaction
			currTrans = currTrans + 1
			if currTrans < len(translist):
				transType = translist[currTrans][0]
				transID = translist[currTrans][1]
				transDetails = translist[currTrans][2]
				
				transIDString = str(transID)
				if len(transIDString) == 1:
					transIDString = "00" + transIDString
				elif len(transIDString) == 2:
					transIDString = "0" + transIDString
				
				string = "E" + transIDString + transDetails
	
	if currID == transID:
		
		if transType == "U": 
			outfile.write(string)
			print("updated: " + string)
			
			#nextTransaction
			currTrans = currTrans + 1
			if currTrans < len(translist):
				transType = translist[currTrans][0]
				transID = translist[currTrans][1]
				transDetails = translist[currTrans][2]
				
				transIDString = str(transID)
				if len(transIDString) == 1:
					transIDString = "00" + transIDString
				elif len(transIDString) == 2:
					transIDString = "0" + transIDString
				
				string = "E" + transIDString + transDetails
				
		elif transType == "D":
			#nextTransaction
			currTrans = currTrans + 1
			if currTrans < len(translist):
				transType = translist[currTrans][0]
				transID = translist[currTrans][1]
				transDetails = translist[currTrans][2]
				
				transIDString = str(transID)
				if len(transIDString) == 1:
					transIDString = "00" + transIDString
				elif len(transIDString) == 2:
					transIDString = "0" + transIDString
				
				string = "E" + transIDString + transDetails
				
		else:
			print("invalid transaction at line:" + line)
	else:
		outfile.write(line)
	
	
	
	line = infile.readline()

transfile.close()
infile.close()
outfile.close()