#polyex2.py
class C1:
	def __init__(self):
		print("C1-Default Constructor")

class C2 (C1):
	def __init__(self):
		print("C2-Default Constructor")
		super().__init__()

class C3 (C2):
	def __init__(self):
		print("C3-Default Constructor")
		super().__init__()


#main program
o3=C3()