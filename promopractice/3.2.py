def HashKey(ThisCountry):
	mySum = 0
	for i in range(len(ThisCountry)):
		mySum = mySum + ord(ThisCountry[i])
	
	ans = mySum % 373 + 1
	return ans


def CreateCountry():
	with open("COUNTRIES.txt","r") as infile:
		line = infile.readline()
		
	for i in range(len(line)):
		if 48 <= ord(line[i]) <= 57: #check if place is digit
			myCountry = line[:i-1]
			myPopulation = line[i:]
			break
	
	myHash = HashKey(myCountry)
	
	newfileArr = []
	
	for j in range(373):
		if j == myHash:
			string = myCountry + " " + myPopulation + "\n"
			newfileArr.append(string)
		else:
			newfileArr.append("\n")
	
	with open("NEWFILE","w") as outfile:
		for line in newfileArr:
			outfile.write(line)
				
##main
CreateCountry()