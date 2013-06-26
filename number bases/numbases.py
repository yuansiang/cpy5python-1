import math

def decToBin(quotient):
	ans=""
	while quotient > 1:
		rem = quotient % 2
		quotient = math.floor(quotient / 2)
		ans = str(rem) + ans
		
	ans = str(quotient) + ans
	return ans

def decToOct(quotient):
	ans=""
	while quotient > 7:
		rem = quotient % 8
		quotient = math.floor(quotient / 8)
		ans = str(rem) + ans
	ans = str(quotient) + ans
	return ans

def decToHex(quotient):
	convert = 0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'
	ans = ""
	while quotient > 15:
		rem = convert[quotient % 16]
		quotient = math.floor(quotient / 16)
		ans = str(rem) + ans
	ans = str(convert[quotient]) + ans
	return ans

def binToDec(num):
	ans = 0
	num = str(num)
	length = len(num)
	for i in range(length):
		ans = ans + int(num[length - i - 1])*2**i
	return ans

def octToDec(num):
	ans = 0
	num = str(num)
	length = len(num)
	for i in range(length):
		ans = ans + int(num[length - i - 1])*8**i
	return ans

def hexToDec(num):
	convert = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
	ans = 0
	num = str(num)
	length = len(num)
	for i in range(length):
		ans = ans + convert[num[length - i - 1]]*16**(i)
	return ans
	
	
##main
print(hexToDec("1e"))