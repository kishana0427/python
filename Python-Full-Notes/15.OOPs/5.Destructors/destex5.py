#here PVM calls Garbage Collector  and  Garbage Collector inturns calls its own destructor for de-allocating the memory space.
#destex5.py
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
eo3=eo2 # deep copy
print("Content of eo2=", eo2.__dict__)
print("Content of eo3=", eo3.__dict__)
print("----------------------------------------------------")
print("No longer interested to maintain eo1 object data")
time.sleep(10)
eo1=None  # here GC will not call __del__(self)
print("No longer interested to maintain eo2 object data")
time.sleep(10)
eo2=None  # here GC will not call __del__(self)
print("Line-29-->Program execution ended:")
# here GC will  call __del__(self)