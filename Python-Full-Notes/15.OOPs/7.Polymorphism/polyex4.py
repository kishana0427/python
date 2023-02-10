#polyex4.py
class C1:
	def setvalues(self,a):  # Original Method
		print("C1-setvalues()")
		print("val of a in setvalues()={}".format(a))
		print("---------------------------------------")

class C2 (C1):  
	def setvalues(self,b):  # Overridden method
		print("C2-setvalues()")
		print("val of b in setvalues()={}".format(b))
		print("---------------------------------------")
		super().setvalues(3000)
class C3 (C2):
	def setvalues(self,c):    # Overridden Method
		print("C3-setvalues()")
		print("val of c in setvalues()={}".format(c))
		print("---------------------------------------")
		super().setvalues(2000)

#main program
o3=C3()
o3.setvalues(1000)