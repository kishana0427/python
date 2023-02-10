#paramconstex.py
class Test:
	def  __init__(self,a,b):  # Parameterized  constructor 
		print("i am from Parameterized constructor:")
		self.a=a
		self.b=b
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
	
# main program
t1=Test(10,20) # Object Creation
t2=Test(100,200)  # Object Creation
t3=Test(1000,2000)  # Object Creation

"""
Output: 
	G:\KVR-PYTHON-11AM\CONSTRUCTOR>py paramconstex.py
i am from Parameterized constructor:
Val of a=10
Val of b=20
i am from Parameterized constructor:
Val of a=100
Val of b=200
i am from Parameterized constructor:
Val of a=1000
Val of b=2000
"""