#here PVM calls Garbage Collector  and  Garbage Collector inturns calls its own destructor for de-allocating the memory space.
#destex1.py
class Employee:
	def __init__(self,eno,ename,sal):
		print("I am from Constructor:")
		self.eno=eno
		self.ename=ename
		self.sal=sal
		print("{}\t{}\t{}".format(self.eno,self.ename,self.sal))

	def	__del__(self): # Programmer-defined Destructor
		print("\nDestructor called by Garbage Collector:")

#main program
print("Line-15-->Program execution Started:")
eo1=Employee(10,"RS",34.56)
eo2=Employee(20,"DR",44.56)
eo3=Employee(30,"MC",24.56)
print("Line-19-->Program execution ended:")
