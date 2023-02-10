#circle2.py
class Circle:
	@classmethod
	def getpi(cls):
		cls.pi=3.14
		return Circle.pi
	def  getrad(self):
		self.r=float(input("Enter Radius:"))

	def  calarea(self):
		ac=Circle.getpi()*self.r**2
		print("Area of Cicrle={}".format(ac))
	def  calcircum(self):
		pc=2*self.getpi()*self.r
		print("Circumference osf Circle={}".format(pc))

#main program
co=Circle()
co.getrad()
co.calarea()
co.calcircum()