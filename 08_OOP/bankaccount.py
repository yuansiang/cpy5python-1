#bankaccount.py

class Account():
	'''Bank account class'''
	
	def __init__(self,account_no,balance):
		'''constructor method'''
		#double underscore makes it a hidden private attribute
		self.__account_no = account_no
		self.__balance = balance
		
	def get_account_no(self):
		'''accessor method to retrieve account no'''
		return self.__account_no
	
	def get_balance(self):
		return self.__balance
	
	def deposit(self,amount):
		'''modifier/mutator method to update balance'''
		self.__balance += amount
		print("")
		
	def withdraw(self,amount):
		self.__balance -= amount
		print("")
	
	#no public method to change account number, for safety because usually you do not change account number after creation
	
	def display(self):
		'''helper/support method to show account info'''
		print("Account No:",self.__account_no)
		print("Balance:",self.__balance)
		
class Savings_Account(Account):
	def __init__(self,account_no,balance,interest):
		super().__init__(account_no,balance)
		self.__interest = interest
		
	def withdraw(self,amount):
		if amount > self.get_balance():
			print("Your account does not have sufficient funds")
		else:
			super().withdraw(amount)
			
	def calc_interest(self):
		self.deposit(self.get_balance() * self.__interest)
			
	def display(self):
		print("Account type: Savings Account")
		super().display()
		print("")
		
class Current_Account(Account):
	def __init__(self,account_no,balance,overdraft_limit):
		super().__init__(account_no,balance)
		self.__overdraft_limit = overdraft_limit
		
	def withdraw(self,amount):
		if (self.get_balance() - amount) < (self.__overdraft_limit * -1):
			print("The amount you have intended to withdraw, ",amount,"has exceeded the overdraft limit for your account, ",self.__overdraft_limit,".")
		else:
			super().withdraw(amount)
			
	def display(self):
		print("Account type: Current Account")
		super().display()
		print("Overdraft limit:",self.__overdraft_limit)
		print("")
	
#main
acct1 = Savings_Account("S01",5000,.1)
acct1.display()
acct1.calc_interest()
acct1.display()
acct1.calc_interest()
acct1.display()
acct1.withdraw(3000)
acct1.display()
acct1.withdraw(3000)
acct1.display()

print("")

acct2 = Current_Account("C01",5000,3000)
acct2.display()
acct2.withdraw(3000)
acct2.display()
acct2.withdraw(3000)
acct2.display()
acct2.withdraw(3000)
acct2.display()