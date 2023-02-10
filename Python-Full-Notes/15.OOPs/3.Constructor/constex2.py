#constex2.py
class Test:
	def  __init__(self):  # default constructor / zero argument constructor
		print("i am from constructor:")
		self.a=10
		self.b=20
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
	
# main program
t1=Test() # Object Creation
