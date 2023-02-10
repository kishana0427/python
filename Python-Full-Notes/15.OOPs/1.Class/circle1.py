#circle1.py
class Circle:
	PI=3.14
	def  getrad(self):
		self.r=float(input("Enter Radius:"))

	def  calarea(self):
		ac=Circle.PI*self.r**2
		print("Area of Cicrle={}".format(ac))
	def  calcircum(self):
		pc=2*self.PI*self.r
		print("Circumference of Circle={}".format(pc))

#main program
co=Circle()
co.getrad()
co.calarea()
co.calcircum()