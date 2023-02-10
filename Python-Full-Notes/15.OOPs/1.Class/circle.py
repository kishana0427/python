#circle.py
class Circle:
	def  getrad(self):
		self.r=float(input("Enter Radius:"))

	def  calarea(self):
		ac=3.14*self.r**2
		print("Area of Cicrle={}".format(ac))
	def  calcircum(self):
		pc=2*3.14*self.r
		print("Circumference of Circle={}".format(pc))

#main program
co=Circle()
co.getrad()
co.calarea()
co.calcircum()