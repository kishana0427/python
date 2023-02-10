#InhProg1.py
class Company:
	def  getcompanydetails(self):
		self.cname="TCS"
		self.caddr="HYD"

class Sunny (Company):  # Single Inheritance
	def  getsunnydet(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Ente Employee Name:")
		self.dsg=input("Enter Designation:")
	def  dispsunnydet(self):
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Designation:{}".format(self.dsg))

#main program
so=Sunny()
print("19-----content of so=",so.__dict__)# 19-----content of so= {}
so.getsunnydet()
print("21---ontent of so=",so.__dict__)# 21---content of so= {'eno': 10, 'ename': 'Sunny', 'dsg': 'SE'}
so.getcompanydetails()
print("23---ontent of so=",so.__dict__)# 23---content of so= {'eno': 10, 'ename': 'Sunny', 'dsg': 'SE', 'cname': 'TCS', 'caddr': 'HYD'}
