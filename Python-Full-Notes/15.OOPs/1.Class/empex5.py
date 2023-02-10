#empex5.py
class Employee:
	@classmethod
	def  getcompanyname(cls):
		cls.cname="TCS"
		cls.getcompanyaddr()
	@classmethod 
	def  getcompanyaddr(cls):
		cls.addr="HYD"
	
	def  getempdet(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")

	def dispempdet(self):
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		Employee.getcompanyname()
		print("Employee Company Name:{}".format(Employee.cname))
		print("Employee Company Name:{}".format(Employee.addr))
#main program
eo1=Employee()
eo1.getempdet()
eo1.dispempdet()
