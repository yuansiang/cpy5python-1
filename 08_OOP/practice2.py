###practice2.py

class Staff():
	
	def __init__(self,staff_id,name,salary):
		self.__staff_id = staff_id
		self.__name = name
		self.__salary = salary
		
	def get_staff_id(self):
		return self.__staff_id
	
	def get_name(self):
		return self.__name
	
	def get_salary(self):
		return self.__salary
	
	def set_salary(self,newSalary):
		self.__salary = newSalary
		
	def compute_salary(self,month):
		return self.__salary
		
	def generate_payroll(self,month):
		print("Staff:",self.get_staff_id())
		print("Name:",self.get_name())
		print("Salary:",self.compute_salary(month))
		print("\n")
	
class FulltimeStaff(Staff):
	
	def __init__(self,staff_id,name,salary):
		super().__init__(staff_id,name,salary)
		
	def compute_salary(self,month):
		salary = self.get_salary()
		if month == "June":
			return "{0:.2f}".format(salary * 1.5)
		elif month == "December":
			return "{0:.2f}".format(salary * 2)
		else:
			return "{0:.2f}".format(salary)
	
class ParttimeStaff(Staff):
	
	def __init__(self,staff_id,name,daily_rate,work_days):
		super().__init__(staff_id,name,daily_rate * work_days)
		self.__daily_rate = daily_rate
		self.__work_days = work_days
		
	def get_daily_rate(self):
		return self.__daily_rate
	
	def set_daily_rate(self,newRate):
		self.__daily_rate = newRate
		
	def get_work_days(self):
		return self.__work_days
	
	def set_work_days(self,newNum):
		self.__work_days = newNum
		
	def compute_salary(self,month):
		salary = self.get_daily_rate() * self.get_work_days()
		return "{0:.2f}".format(salary)
		

	