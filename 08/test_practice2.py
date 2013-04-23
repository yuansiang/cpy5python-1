###test_practice2.py

from practice2 import *
import unittest

class MyTestCase(unittest.TestCase):
	
	def setUp(self):
		self.staff1 = FulltimeStaff("S01","Lim Ah Seng",3000)
		self.staff2 = ParttimeStaff("P01","Tan Di Sheng",150,20)
		
	def test_compute_salary1(self):
		self.assertAlmostEqual(self.staff1.compute_salary("June"), 4500)
	
	def test_compute_salary2(self):
		self.assertAlmostEqual(self.staff1.compute_salary("December"), 6000)


	def tearDown(self):
		self.staff1 = None
		self.staff2 = None
	
##main
if __name__ == '__main__':
	unittest.main(exit=False)
	

#staff1 = FulltimeStaff("S01","Lim Ah Seng",3000)
#staff1.generate_payroll("June")
#
#staff2 = ParttimeStaff("P01","Tan Di Sheng",150,20)
#staff2.generate_payroll("June")
#staff2.set_daily_rate(30)
#staff2.generate_payroll("May")