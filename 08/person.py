###person.py

class Person():
	def __init__(self,pid,name):
		self.__pid = pid
		self.__name = name
		
	def get_pid(self):
		return self.__pid
	
	def get_name(self):
		return self.__name
	
	def display(self):
		print("ID:",self.__pid)
		print("Name:",self.__name)
		
class Student(Person):
	def __init__(self,pid,name,classid):
		super().__init__(pid,name)
		self.__classid = classid
		
	def get_classid(self):
		return self.__classid
	
	def set_classid(self,new_classid):
		self.__classid = new_classid
		
	def display(self):
		super().display()
		print("Class:",self.__classid)
		
class Staff(Person):
	def __init__(self,pid,name,department):
		super().__init__(pid,name)
		self.__department = department
		
	def get_department(self):
		return self.__department
	
	def set_classid(self,new_department):
		self.__department = new_department
		
	def display(self):
		super().display()
		print("Class:",self.__department)
		
###main

student1 = Student("S01","Lim Ah Seng","13Y5C23")
student1.display()

staff1 = Staff("A05","Robert Yeo","Computing")
staff1.display()

person_list = []
person_list.append(student1)
person_list.append(staff1)
for person in person_list:
	person.display()