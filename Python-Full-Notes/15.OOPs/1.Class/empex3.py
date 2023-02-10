#empex3.py
class Employee:
	cname="IBM"  # Class Level Data Member
	def   getempdet(self ):
		print("-"*50)
		print("Id of (sellf) in getempdet()=",id(self))
		self.eno=int(input("Enter  Employee Number:"))
		self.ename=input("Enter  Employee Name:")
		self.sal=float(input("Enter  Employee Salary:"))
		print("-"*50)
	def dispempdet(self):
		print("----------------------------------------------")
		print("Id of (self) in dispempdet()=",id(self))
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Salary:{}".format(self.sal))
		print("Employee Comp Name:{}".format(Employee.cname))
		print("Employee Comp Addr:{}".format(Employee.caddr))
		print("----------------------------------------------")		

#MAIN PROGRAM
Employee.caddr="HYD" # Class Level Data Member
#create First object
eo1=Employee()
print("id of eo1 in main program=",id(eo1))
print("Enter First Emplyee Details")
eo1.getempdet()
#create Second object
eo2=Employee()
print("id of eo2 in main program=",id(eo2))
print("Enter Second Emplyee Details")
eo2.getempdet()
#create third object
eo3=Employee()
print("id of eo3 in main program=",id(eo3))
print("Enter Third Emplyee Details")
eo3.getempdet()
#add Instance Data Members
print("First Employee Data")
eo1.dispempdet()	
print("Second Employee Data")
eo2.dispempdet()
print("Third Employee Data")
eo3.dispempdet()