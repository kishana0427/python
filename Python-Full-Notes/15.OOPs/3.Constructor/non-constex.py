#non-constex.py
class Employee:
	def   getempvalues(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")

#main program
eo1=Employee()
print("Content of eo1 before reading the data=",eo1.__dict__) # { }
eo1.getempvalues() # explicitly we are calling one function for reading the data
print("Content of eo1 after reading the data=",eo1.__dict__) # {-----, ------)