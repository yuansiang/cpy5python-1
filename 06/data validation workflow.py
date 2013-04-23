#valid range for age 1 - 100

#set boolean valid_age to false
valid_age = False
#loop until valid_age is true
while not valid_age:
#    get age
	age = input("Enter your age:")
#    if empty input display empty input message and allow re-entry
	if len(age) == 0:
		print("Empty input. Try again.")
		
	elif age == "quit":
		quit()
			
#    if not a number display wrong data type and allow re-entry
	elif not age.isdigit():
		print("Age is a number. Try again.")
#    if not within valid range display invalid range and allow re-entry
	elif not 0 < int(age) <= 100:
		print("Are you a human? Enter between 1 to 100")
	
	
#    else set valid_age to true
	else:
			valid_age = True


