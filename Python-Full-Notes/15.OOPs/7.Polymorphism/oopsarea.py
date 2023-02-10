#oopsarea.py
class Circle:
	def  area(self,r): # original method
		ac=3.14*r**2
		print("Area of Circle={}".format(ac))
class Square:
	def area(self,s): # original method
		sa=s**2
		print("Area of Square={}".format(sa))
		print("-"*50)
class Rect(Square,Circle):
	def area(self,l,b):
		ra=l*b
		print("Area of Rect={}".format(ra))
		print("-"*50)
		Square.area(self,float(input("Enter Side Value:")) )
		Circle.area(self,float(input("Enter the Radious:")) )
#main program
l,b=int(input("Enter Length:")),int(input("Enter Breadth:"))
ro=Rect()
ro.area(l,b)




