#empex1.py
class Employee:
	def  __init__(self,eno,ename,sal):   # Parametrized Cons
		self.eno=eno
		self.ename=ename
		self.sal=sal
		print("{}\t{}\t{}".format(self.eno,self.ename,self.sal))

#main program
eo1=Employee(10,"RS",5.6)
eo2=Employee(20,"JG",4.6)
eo3=Employee(30,"DR",7.6)