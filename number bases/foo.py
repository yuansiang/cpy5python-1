###foo.py

import math

def dec_to_bin(num):
	ans = ""
	quotient = num
	while quotient > 1:
		rem = int(quotient % 2)
		ans = str(rem) + ans
		quotient = math.floor(quotient/2)
		
	ans = str(int(quotient)) + ans
	
	return ans

def dec_to_oct(num):
	ans = ""
	quotient = num
	while quotient > 7:
		rem = int(quotient % 8)
		ans = str(rem) + ans
		quotient = math.floor(quotient/8)
		
	ans = str(int(quotient)) + ans
	
	return ans

def dec_to_hex(num):
	convert = 0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'
	ans = ""
	quotient = num
	while quotient > 15:
		rem = convert[int(quotient % 15)]
		ans = str(rem) + ans
		quotient = math.floor(quotient/15)
		
	ans = str(convert[int(quotient)]) + ans
	
	return ans

def bin_to_oct(num):
	num = str(num)
	length = len(num)
	ans = 0
	for i in range(length):
		ans = ans + int(num[length - i - 1]) * 8 ** i
	return ans

def bin_to_dec(num):
	num = str(num)
	length = len(num)
	ans = 0
	for i in range(length):
		ans = ans + int(num[length - i - 1]) * 2 ** i
	return ans

##main
print(dec_to_hex(29))