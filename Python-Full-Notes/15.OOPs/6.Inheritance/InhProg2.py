#InhProg2.py
class Company:
	def  getcompanydetails(self):
		self.cname="TCS"
		self.caddr="HYD"

class Employee (Company):  # Single Inheritance
	def  getempdet(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Ente Employee Name:")
		self.dsg=input("Enter Designation:")
		self.getcompanydetails() # calling base class method from derived class
	def  dispempdet(self):
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Designation:{}".format(self.dsg))

#main program
so=Employee()
print("Content of so----line-20",so.__dict__)
so.getempdet()
print("Content of so----line-22",so.__dict__)