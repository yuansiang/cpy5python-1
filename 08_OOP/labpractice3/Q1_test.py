###Q1_test.py

from Q1 import *
import unittest

class MyTestCase(unittest.TestCase):
	
	def setUp(self):
		scoreTable = ScoreTable())
		
	def test_createBowler1(self):
		self.assertEqual(self.staff1.compute_salary("June"), "4500.00")
	
	def test_compute_salary2(self):
		self.assertEqual(self.staff1.compute_salary("December"), "6000.00")
		
	def test_compute_salary3(self):
		self.assertEqual(self.staff2.compute_salary("December"), "3000.00")
		
	def test_setSalary(self):
		self.staff1.set_salary(2000)
		self.assertEqual(self.staff1.compute_salary("April"),"2000.00")
		
	def test_set_daily_rate(self):
		self.staff2.set_daily_rate(300)
		self.assertEqual(self.staff2.compute_salary("Bla"),"6000.00")
		
	def test_set_work_days(self):
		self.staff2.set_work_days(10)
		self.assertEqual(self.staff2.compute_salary("Ahh"),"1500.00")


	def tearDown(self):
		self.staff1 = None
		self.staff2 = None
	
##main
if __name__ == '__main__':
	unittest.main(exit=False)