#polyex9.py
class C1:
	def  x(self):
		print("C1-x()")
class C2(C1):
	def  x(self):
		print("C2-x()")
class C3(C1):
	def  x(self):
		print("C3-x()")
class C4(C2,C3):
	def  x(self):
		print("C4-x()")
class C5(C4):
	def  x(self):
		print("C5-x()")
		C1.x(self)
		C2.x(self)
		C3.x(self)
		super().x()

#main program
o5=C5()
o5.x()
