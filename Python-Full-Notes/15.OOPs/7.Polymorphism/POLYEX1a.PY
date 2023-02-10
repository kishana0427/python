#polyex1a.py
class IntSum:
	def   sumop(self): #Original Method
		print("-"*40)
		a=int(input("Enter First int Value:"))
		b=int(input("Enter Second int Value:"))
		c=a+b
		print("sum of integers={}".format(c))
		print("-"*40)
		
class StrSum(IntSum):
	def  sumop(self):  # Overridden method
		print("="*60)
		a=input("Enter First Str Value:")
		b=input("Enter Second str Value:")
		c=a+b
		print("sum of strs={}".format(c))
		print("="*60)
		super().sumop() # calling Base Class method from intermediate base class

class ComplexSum(StrSum):
	def  sumop(self):  # Overridden method
		print("*"*60)
		a=complex(input("Enter First Complex Value:"))
		b=complex(input("Enter Second Complex Value:"))
		c=a+b
		print("sum of complex values={}".format(c))
		print("*"*60)
		super().sumop() # calling Intermediate Base Class method from derived class
		
#main program
cc=ComplexSum()
cc.sumop()