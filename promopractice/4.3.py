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
	
def romanToDec(num):
	ans = 0
	for i in range(len(num)):
		if num[i] == 'X':
			ans = ans + 10
		elif num[i] == 'V':
			ans = ans + 5
		elif num[i] == 'I':
			if i < len(num) - 1:
				if num[i+1] == 'X' or num[i+1] == 'V':
					ans = ans - 1
				else:
					ans = ans + 1
			else:
					ans = ans + 1
		else:
			print("Error: Must contain 'X', 'V' and 'I' only. No spaces.")
			return -1
	return ans

##main
def validateRoman(num):
	num = romanToDec(num)
	if num == -1:
		return False
	if num > 20:
		print("Roman numeral must not be greater than 20")
		return False
	return True

firstNum = input("input first Roman numeral:")
while not validateRoman(firstNum):
	firstNum = input("input first Roman numeral:")

secondNum = input("input second Roman numeral:")
while not validateRoman(secondNum):
	secondNum = input("input second Roman numeral:")

mySum = romanToDec(firstNum) + romanToDec(secondNum)
print(decToRoman(mySum))