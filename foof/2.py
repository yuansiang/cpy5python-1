import re

pattern = re.compile("[0-9A-Za-z]{2}-[0-9A-Za-z]{2}-[0-9A-Za-z]{4}")
DD = re.compile("[0-9]{2}")
YYYY = re.compile("[0-9]{4}")
	
running = True

while running:
	validated = True
	line = input("\ndate format DD-MM-YYYY\n")
	if(line == ""): 
		print("please input something")
	else:
		
		if not re.match(pattern,line):
			print("Date format must be DD-MM-YYYY")
			validated = False
		else:
			if not re.match(DD,line[0:2]):
				print("DD must be a 2 character integer")
				validated = False
			else:
				date = int(line[0:2])
				if not 1 <= date <= 31:
					print("DD must be an integer between 1 and 31 inclusive")
					validated = False
				
			if not re.match(DD,line[3:5]):
				print("MM must be a 2 character integer")
				validated = False
			else:
				month = int(line[3:5])
				if not 1 <= month <= 12:
					print("MM must be an integer between 1 and 12 inclusive")
					validated = False
					
			if not re.match(YYYY,line[6:10]):
				print("YYYY must be a 4 character integer")
				validated = False

		
		
			
		if validated:
			print("validated")
			running = False
		else:
			print("not validated")