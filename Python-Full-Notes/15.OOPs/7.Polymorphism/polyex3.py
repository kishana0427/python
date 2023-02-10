#polyex3.py
class C1:
	def __init__(self,a):  # Original Constructor
		print("C1-Parameterized Constructor")
		print("val of a in C1={}".format(a))
		print("---------------------------------------")

class C2 (C1):  
	def __init__(self,b):  # Overridden Constructor
		print("C2-Parameterized Constructor")
		print("val of b in C2={}".format(b))
		print("---------------------------------------")
		super().__init__(300)
class C3 (C2):
	def __init__(self,c):    # Overridden Constructor
		print("C3-Parameterized Constructor")
		print("val of c in C3={}".format(c))
		print("---------------------------------------")
		super().__init__(200)
#main program
o3=C3(100)