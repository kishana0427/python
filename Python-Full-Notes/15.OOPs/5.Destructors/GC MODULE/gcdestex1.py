#here PVM calls Garbage Collector  and  Garbage Collector inturns calls its own destructor for de-allocating the memory space.
#gcdestex1.py
import gc
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
print("Line-15-->Is Gc is Enabled / Running?=",gc.isenabled())#True
print("Line-16-->Program execution Started:")
gc.disable()
print("Line-19-->Is Gc is Enabled / Running?=",gc.isenabled())#False
eo1=Employee(10,"RS",34.56)
eo2=Employee(20,"DR",44.56)
eo3=Employee(30,"MC",24.56)
print("Line-23-->Program execution ended:")
#Definitely GC calls __del__(self)