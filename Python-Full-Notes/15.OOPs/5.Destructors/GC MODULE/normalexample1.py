#normalexample1.py
import gc
class Employee:
	def __init__(self,eno,ename,sal):
		print("I am from Constructor:")
		self.eno=eno
		self.ename=ename
		self.sal=sal
		print("{}\t{}\t{}".format(self.eno,self.ename,self.sal))


#main program
print("Line-12-->Is Gc is Enabled / Running?=",gc.isenabled())#True
print("Program execution Started:")
gc.disable()
eo1=Employee(10,"RS",34.56)
eo2=Employee(20,"DR",44.56)
eo3=Employee(30,"MC",24.56)
print("Program execution ended:")
#here PVM calls Garbage Collector inturns calls its own destructor for de-allocating the memory space.