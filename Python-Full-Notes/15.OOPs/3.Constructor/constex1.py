#constex1.py
class Employee:
	def   __init__(self):  # constructor Definition---object initlization
		print("I am from constructor")
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")

#main program
eo1=Employee()  # object creation----one function is calling --- def   __init__(self)
print("Content of eo1 before reading the data=",eo1.__dict__) 