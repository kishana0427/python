#InhProg6.py
class Teacher:
	def  getTeacherdet(self):
		self.tno=int(input("Enter Teacher Number:"))
		self.tname=input("Enter Teacher Name:")
	def dispteacherdet(self):
		print("Teacher Number:{}".format(self.tno))
		print("Teacher Name:{}".format(self.tname))

class Company:
	def  getcompdet(self):
		self.cname=input("Enter Comp Name:")
		self.caddr=input("Enter Company Address:")
	def dispcompdet(self):
		print("Comp Name:{}".format(self.cname))
		print("Company Address:{}".format(self.caddr))

class Student (Teacher,Company):
	def  getstuddet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self. getTeacherdet()
		self.getcompdet()
	def dispstuddet(self):
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		self.dispcompdet()
		self.dispteacherdet()

#main program
so=Student()
so.getstuddet()
print("-"*40)
so.dispstuddet()
print("-"*40)