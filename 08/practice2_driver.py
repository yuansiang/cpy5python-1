###practice2_driver.py

from practice2 import *

staff1 = FulltimeStaff("S01","Lim Ah Seng",3000)
staff1.generate_payroll("June")

staff2 = ParttimeStaff("P01","Tan Di Sheng",150,20)
staff2.generate_payroll("June")
staff2.set_daily_rate(30)
staff2.generate_payroll("May")