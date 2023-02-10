#defaultconstex.py
class Test:
	def  __init__(self):  # default constructor / zero argument constructor
		print("i am from default constructor:")
		self.a=10
		self.b=20
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
	
# main program
t1=Test() # Object Creation
t2=Test()  # Object Creation
t3=Test()  # Object Creation

""""
Output
----------
G:\KVR-PYTHON-11AM\CONSTRUCTOR>py defaultconstex.py
i am from default constructor:
Val of a=10
Val of b=20
i am from default constructor:
Val of a=10
Val of b=20
i am from default constructor:
Val of a=10
Val of b=20  """