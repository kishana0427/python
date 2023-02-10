#InhProg4.py
class Company: # Base Class
	def  getcompanydetails(self):
		self.cname="TCS"
		self.caddr="HYD"
	def dispcompdet(self):
		print("Employee Company Name:{}".format(self.cname))
		print("Employee Company address:{}".format(self.caddr))
class Sunny (Company):  # Single Inheritance
	def  getsunnydet(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Ente Employee Name:")
		self.dsg=input("Enter Designation:")
		self.getcompanydetails() # calling base class method from derived class
	def  dispsunnydet(self):
		print("-"*40)
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Designation:{}".format(self.dsg))
		self.dispcompdet()
		print("-"*40)
#main program
so=Sunny()
so.getsunnydet()
so.dispsunnydet()
