#polyex8.py
class C1:
	def __init__(self,a):  # Original Constructor
		print("C1-Parameterized Constructor")
		print("val of a in C1={}".format(a))
		print("---------------------------------------")

class C2:  
	def __init__(self,b):  # Original Constructor
		print("C2-Parameterized Constructor")
		print("val of b in C2={}".format(b))
		print("---------------------------------------")
		
class C3 (C1,C2):
	def __init__(self,c):    # Overridden Constructor
		print("C3-Parameterized Constructor")
		print("val of c in C3={}".format(c))
		print("---------------------------------------")
		C2.__init__(self,500)
		C1.__init__(self,600)
		
#main program
o3=C3(100)