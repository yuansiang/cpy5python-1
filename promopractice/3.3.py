def HashKey(ThisCountry):
	mySum = 0
	for i in range(len(ThisCountry)):
		mySum = mySum + ord(ThisCountry[i])
	
	ans = mySum % 373 + 1
	return ans


def LookUpCountry():
	uinput = input("Country Name:")
	uaddress = HashKey(uinput)
	
	with open("NEWFILE","r") as infile:
		for i in range(373):
			if i == uaddress:
				print(i,infile.readline())
			else:
				infile.readline()
				
##main
LookUpCountry()