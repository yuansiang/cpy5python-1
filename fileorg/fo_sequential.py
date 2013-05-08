###fo_sequential.py

import datetime

def menu():
	print("[1] Search")
	print("[2] Update")
	print("[3] Create new account")
	print("[0] Quit")
	
def search():
	try:
		pass
	except IOError:
		# input file read error
		print("Cannot read from accounts database ACCOUNTS.DAT")
		
def update():
	try:
		pass
	except IOError:
		# input file read error
		print("Cannot write to accounts database ACCOUNTS.DAT")

def create():
	try:
		pass
	except IOError:
		# input file read error
		print("Cannot write to accounts database ACCOUNTS.DAT")

##main
option = "1"
while option != "0":
	menu()
	option = input("Enter option:")
	if option == "1":
		search()
	elif option == "2":
		update()
	elif option == "3":
		create()
		