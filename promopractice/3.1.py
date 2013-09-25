def HashKey(ThisCountry):
	mySum = 0
	for i in range(len(ThisCountry)):
		mySum = mySum + ord(ThisCountry[i])
	
	ans = mySum % 373 + 1
	return ans

myCountry = input("Input Country:")
print(HashKey(myCountry))