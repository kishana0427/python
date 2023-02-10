#empex2.py
class Employee:
	def  __init__(self,eno=5,ename="RS",sal=9.9):   # Parametrized Cons
		self.eno=eno
		self.ename=ename
		self.sal=sal
		print("{}\t{}\t{}".format(self.eno,self.ename,self.sal))
#main program
eo=Employee()
eo1=Employee(10,"VK",5.6)
eo2=Employee(20,"AN",4.6)
eo3=Employee(30,"SN",7.6)
eo4=Employee(40,"AJ",7.6)
eo5=Employee(50,"PN",7.6)