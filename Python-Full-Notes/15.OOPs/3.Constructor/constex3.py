#constex3.py
class Test:
	def  __init__(self, a,b):  # Parameterized constructor
		print("i am from Parameterized constructor:")
		self.a=a
		self.b=b   # here self.a and self.b are called Instance variables
		c=self.a+self.b  # here 'c' is called Local Variable
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("sum=",c)
	
# main program
x=float(input("Enter the value of x:"))
y=float(input("Enter the value of y:"))
t1=Test(x,y) # Object Creation
