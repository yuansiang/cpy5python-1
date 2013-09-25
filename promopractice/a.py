import datetime

def eidIsPresent(eid):
	with open("EMPLOYEE.dat","r") as infile:
		
		line = infile.readline()
		while line != "":
			if line[0:4] == eid:
					return True
			line = infile.readline()
		else:
			return False

def search():
	with open("EMPLOYEE.dat","r") as infile:
		eid = input("Enter Employee ID: ")
		while not validateEID(eid):
			eid = input("Enter Employee ID: ")
			
		line = infile.readline()
		while line != "":
			if line[0:4] == eid:
				print(line)
				return
			line = infile.readline()
		else:
			print("Employee ID not found in database")

def add():
	infile = open("EMPLOYEE.dat","r")
	outfile = open("TRANSACTIONS.dat","a")
	
	
	#collect user input
	eid = input("Enter Employee ID: ")
	while not validateEID(eid):
		eid = input("Enter Employee ID: ")
	
	if eidIsPresent(eid):
		print("Employee ID already exists in database! Please enter an ID not currently in use.")
		return
	
	name = input("Enter Employee name (under 15 characters): ")
	while not validateName(name):
		name = input("Enter Employee name (under 15 characters): ")
	
	department = input("Enter Employee department: ")
	while not validateDepartment(department):
		department = input("Enter Employee department: ")
		
	salary = input("Enter Employee salary: ")
	while not validateSalary(salary):
		salary = input("Enter Employee salary: ")

	timestamp = datetime.datetime.now()
	timestamp = timestamp.strftime("%Y%m%d%H%M%S")
	
	transactionType = "A"
	
	string = "{0}{1}{2}{3:15}{4:5}{5:4}\n".format(timestamp,transactionType,eid,name,department,salary)
		
	outfile.write(string)
	

def update():
	infile = open("EMPLOYEE.dat","r")
	outfile = open("TRANSACTIONS.dat","a")
	
	
	#collect user input
	eid = input("Enter Employee ID: ")
	while not validateEID(eid):
		eid = input("Enter Employee ID: ")
	
	if not eidIsPresent(eid):
		print("Employee ID does not exist in database! You can only update existing entries, or you can add an entry instead.")
		return
	
	name = input("Enter Employee name (under 15 characters): ")
	while not validateName(name):
		name = input("Enter Employee name (under 15 characters): ")
	
	department = input("Enter Employee department: ")
	while not validateDepartment(department):
		department = input("Enter Employee department: ")
		
	salary = input("Enter Employee salary: ")
	while not validateSalary(salary):
		salary = input("Enter Employee salary: ")

	timestamp = datetime.datetime.now()
	timestamp = timestamp.strftime("%Y%m%d%H%M%S")
	
	transactionType = "U"
	
	string = "{0}{1}{2}{3:15}{4:5}{5:4}\n".format(timestamp,transactionType,eid,name,department,salary)
		
	outfile.write(string)
	
def delete():
	infile = open("EMPLOYEE.dat","r")
	outfile = open("TRANSACTIONS.dat","a")
	
	
	#collect user input
	eid = input("Enter Employee ID: ")
	while not validateEID(eid):
		eid = input("Enter Employee ID: ")
	
	if not eidIsPresent(eid):
		print("Employee ID does not exist in database! You can only delete existing entries.")
		return
	
	timestamp = datetime.datetime.now()
	timestamp = timestamp.strftime("%Y%m%d%H%M%S")
	
	transactionType = "D"
	
	string = "{0}{1}{2}\n".format(timestamp,transactionType,eid)
		
	outfile.write(string)

def validateEID(eid):
	if eid == "":
		print("empty input!")
		return False
	if len(eid) != 4:
		print("eid must be 4 characters in length")
		return False
	if eid[0] != "E":
		print("first character of EID must be 'E'")
		return False
	try:
		nnn = int(eid[1:4])
		if 1<= nnn <= 500:
			return True
		else:
			print("EID must be in the form of E<NNN> where NNN is an integer between 1 and 500")
			return False
	except:
		print("EID must be in the form of E<NNN> where NNN is an integer")
		return False
	
def validateName(name):
	if name == "":
		print("empty input!")
		return False
	if len(name) > 15:
		print("name must be 15 or less characters")
		return False
	return True

def validateDepartment(dpm):
	if dpm == "":
		print("empty input!")
		return False
	if len(dpm) > 5:
		print("Department must be 5 or less characters")
		return False
	return True

def validateSalary(salary):
	if salary == "":
		print("empty input!")
		return False
	try:
		salary = int(salary)
		if salary > 9999:
			print("Salary must be less than 10000!")
			return False
		return True
	except:
		print("salary must be an integer!")
		return False
	
##main
looping = True
while looping:
	print("[1] Search")
	print("[2] Add")
	print("[3] Update")
	print("[4] Delete")
	print("[0] Quit")
	uinput = input()
	
	if uinput == "1":
		search()
	elif uinput =="2":
		add()
	elif uinput == "3":
		update()
	elif uinput == "4":
		delete()
	elif uinput == "0":
		looping = False
	else:
		print("user input invalid!")