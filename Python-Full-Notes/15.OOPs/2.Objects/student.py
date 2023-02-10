#student.py---file name treated as module name 
class Student:
	def getstuddet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		self.cname=input("Enter Student College Name:")
	
	def dispstuddet(self):
		print("{}\t{}\t{}\t{}".format(self.sno, self.sname, self.marks, self.cname))
