import re

pattern = re.compile("[A-Z]{2}[0-9]{3}")
AA = re.compile("[A-Z]{2}")
NNN = re.compile("[0-9]{3}")
	
running = True

while running:
	line = input("\nrecord key format AANNN (where A is a uppercase letter and NNN is an integer in the range 1 to 999) \n")
	if(line == ""): 
		print("please input a key")
	else:
		if re.match(pattern,line):
			number = line[2:5]
			if number == "000":
				print("NNN must be an integer of value 1 to 999")
			else:
				print("validated")
				running = False
		else:
			if not re.match(AA,line[0:2]):
				print("A must be a capital letter")
			if not re.match(NNN,line[2:5]):
				print("NNN must be an integer")
			print("not validated")