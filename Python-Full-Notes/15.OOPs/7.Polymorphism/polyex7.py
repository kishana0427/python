#polyex7.py
class C1:
	def __init__(self):
		print("C1-Default Constructor")

class C2 :
	def __init__(self):
		print("C2-Default Constructor")
	
class C3 (C1,C2):
	def __init__(self):
		print("C3-Default Constructor")
		C1.__init__(self)
		C2.__init__(self)
		
#main program
o3=C3()