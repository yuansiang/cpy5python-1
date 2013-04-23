import re

##get gender
#gender = input("Insert gender:")
#
#pattern = re.compile("[MmFf]")
#
#if not pattern.match(gender):
#	print("invalid gender")
#else:
#	print("ok")

valid_nric = False

while not valid_nric:
	#get nric
	nric = input("Input NRIC:")
	
	if(nric == "quit"):
		quit()
	
	# ^ - starts with, {n} exactly n times, $ - ends with
	pattern = re.compile("^[sS][0-9]{7}[a-zA-Z]$")
	
	if not pattern.match(nric):
			print("Invalid NRIC")
	else:
			print("ok")
			valid_nric = True
