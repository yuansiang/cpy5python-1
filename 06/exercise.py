valid_nric = False
valid_name = False
valid_class = False
valid_gender = False
valid_DOB = False
valid_weight = False
valid_height = False

while not valid_nric:
	nric_pattern = re.compile("^[sS][0-9]{7}[a-zA-Z]$")
	
	#get nric
	nric = input("Input NRIC:")
	
	if(nric == "quit"):
		quit()
	
	elif(len(nric)==0):
		print("No input")

	elif not nric_pattern.match(nric):
			print("Invalid NRIC")
	else:
			valid_nric = True

while not valid_name:
	name_pattern = re.compile("[a-zA-Z]")
	
	name = input("Input Name:")
	
	if(name == "quit"):
		quit()
	
	elif not name_pattern.match(name):
			print("Name must only contain alphabets")
	else:
			valid_nric = True

while not valid_class:
	className = input("Input Class:")
	
	if(className == "quit"):
		quit()
	
	pattern = re.compile("^[0-9]{2}Y[0-9]C[0-9]{2}$")
	#^[0-9]{2}[Y]{1}[0-9]{1}[C]{1}[0-9]{2}$
	
	elif not pattern.match(className):
			print("Class must be in this form <YY>Y<9>C<99> eg 13Y5C23")
	else:
			valid_class = True

while not valid_gender:
	gender = input("Insert gender:")
	
	if(gender=="quit"):
		quit()
	
	pattern = re.compile("[MmFf]")
	
	if not pattern.match(gender):
		print("invalid gender")
	else:
		valid_gender = True

while not valid_DOB:
	DOB = input("Input Date of Birth:")
	
	if(DOB == "quit"):
		quit()
	
	pattern = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}")
	
	if not pattern.match(className):
			print("Date must be in the form DD-MM-YYYY)
	else:
			valid_DOB = True