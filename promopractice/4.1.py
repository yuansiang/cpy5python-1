def decToRoman(num):
	ans = ""

	while num >= 10:
		ans += "X"
		num = num - 10
	
	if num == 9:
		ans += "IX"
		return ans
	
	while num >= 5:
		ans += "V"
		num = num - 5
	
	if num == 4:
		ans += "IV"
		return ans
	
	while num > 0:
		ans += "I"
		num = num - 1
		
		
	return ans
	

##main

numValidated = False
while not numValidated:
	num = input("Input integer between 1 and 20:")
	if num == "":
		print("Must input a value!") #presence check
	try:
		num = int(num)
		if 1 <= num <= 20:
			numValidated = True
		else:
			print("number must be between 1 and 20 inclusive") #range check
	except:
		print("Input must be an integer!") #datatype check

print(decToRoman(num))