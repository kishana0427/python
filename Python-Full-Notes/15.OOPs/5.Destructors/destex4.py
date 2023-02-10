#here PVM calls Garbage Collector  and  Garbage Collector inturns calls its own destructor for de-allocating the memory space.
#destex4.py
import time
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
eo2=eo1 # Deep Copy
eo3=eo2 # Deep Copy
print("Line-20-->Program execution ended:")
# Here GC calls _del__(self)  one time