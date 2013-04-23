import re
import datetime

def check_nric(nric):
	numbers = nric[1:8]
	if(nric[0]=='s' or nric[0]=='S' or nric[0]=='t' or nric[0]=='T'):
		check_map = {0:'J',1:'Z', 2:'I', 3:'H', 4:'G', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}
	else:
		check_map = {0:'X', 1:'W', 2:'U', 3:'T', 4:'R', 5:'Q', 6:'P', 7:'N', 8:'M', 9:'L', 10:'K'}
	
	weights = [2,7,6,5,4,3,2]
	
	sum_products = 0
	for i in range(7):
		sum_products = sum_products + (int(numbers[i]) * weights[i])
	remainder = sum_products % 11
	
	if(check_map[remainder]==nric[8] or check_map[remainder]==str(nric[8]).upper()):
		return True
	else:
		return False
	
#main
valid_nric = False

while not valid_nric:
	myNRIC = input("Input NRIC:")
	
	if(myNRIC=="quit"):
		quit()
	
	# ^ - starts with, {n} exactly n times, $ - ends with
	nricPattern = re.compile("^[sStTfFgG][0-9]{7}[a-zA-Z]$")
	
	if not nricPattern.match(myNRIC):
			print("Invalid NRIC. NRIC must in the form of S1234567A")
	elif not (check_nric(myNRIC)):
			print("Invalid NRIC. You trying to spoof the system? :P")
	else:
		print("Valid NRIC. Proceed.")