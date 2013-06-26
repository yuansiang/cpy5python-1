import datetime

#get current system date
current_date = datetime.datetime.now()

#print(current_date.month)

print(current_date.strftime("%H:%M:%S, %a %d-%b-%Y"))

#print(datetime.datetime.now())

#d = input("Enter date in DD-MM-YYYY format: ")
 
#try:
#    valid_date = datetime.datetime.strptime(d, "%d-%m-%Y")
#except ValueError:
#    print("Invalid date.")
#		
