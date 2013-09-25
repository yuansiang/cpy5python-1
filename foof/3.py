import re

pattern = re.compile("[0-9A-Za-z]{2}:[0-9A-Za-z]{2}:[0-9A-Za-z]{2}")
HH = re.compile("[0-9]{2}")
	
running = True

while running:
	validated = True
	line = input("\ntime format HH:MM:SS\n")
	if(line == ""): 
		print("please input something")
	else:
		
		if not re.match(pattern,line):
			print("Time format must be HH:MM:SS")
			validated = False
		else:
			if not re.match(HH,line[0:2]):
				print("HH must be a 2 character integer")
				validated = False
			else:
				hour = int(line[0:2])
				if not 0 <= hour <= 23:
					print("DD must be an integer between 0 and 23 inclusive")
					validated = False
				
			if not re.match(HH,line[3:5]):
				print("MM must be a 2 character integer")
				validated = False
			else:
				minute = int(line[3:5])
				if not 0 <= minute <= 59:
					print("MM must be an integer between 0 and 59 inclusive")
					validated = False
					
			if not re.match(HH,line[6:8]):
				print("SS must be a 2 character integer")
				validated = False
			else:
				second = int(line[6:8])
				if not 0 <= second <= 59:
					print("SS must be an integer between 0 and 59 inclusive")
					validated = False

		
		
			
		if validated:
			print("validated")
			running = False
		else:
			print("not validated")