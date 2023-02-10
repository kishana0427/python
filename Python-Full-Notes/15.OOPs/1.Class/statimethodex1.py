#statimethodex1.py
#This program demonstartes the static method and importance.
class Employee:
	def    getempdet(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Sal:"))

class Student:
	def   getstuddata(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		self.cname=input("Enter Student College Name:")

class ShowInfo:
	@staticmethod
	def   dispinfo( x ):
		print("-"*40)
		for k,v in x.__dict__.items():
			print("\t{}\t{}".format(k,v))
		print("-"*40)

#main program
eo1=Employee()
eo1.getempdet()
print("-------------------------------------------")
so1=Student()
so1.getstuddata()
print("Employee Information:")
so=ShowInfo()
ShowInfo.dispinfo(eo1)
print("Student Information:")
ShowInfo.dispinfo(so1)
