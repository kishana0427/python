#shapesarea.py
def  rectarea():
	l=float(input("Enter Length:"))
	b=float(input("Enter Breadth:"))
	print("Area of Rect=",(l*b))
def  squarearea():
	s=float(input("Enter Side:"))
	print("Area of Square=",(s**2))
def  circlearea():
	r=float(input("Enter Radius:"))
	print("Area of Circle=",(3.14*r**2))
def  trianglearea():
	b=float(input("Enter Base of triangle:"))
	h=float(input("Enter Hight of triangle:"))
	print("Area of Triangle=",(1/2)*b*h)
def menu():
	print("==================================")
	print("\tArea of Different Shapes")
	print("==================================")
	print("\t1.Circle")
	print("\t2.Rect")
	print("\t3.Square")
	print("\t4.Triangle")
	print("\t9.main menu")
	print("\t5.Exit")
	print("==================================")

#main program
menu()
while True:
	ch=int(input("Enter ur Choice:"))
	if ch<=0 or ch>9 or ch in[6,7,8]:
		print("Invalid input...Select Correct Choice!!!")
		ch=int(input("Enter ur Choice : "))
	elif ch in [1,2,3,4,5,9]:
		match ch:
			case 1: circlearea()
			case 2:  rectarea()
			case 3:  squarearea()
			case 4: trianglearea()
			case 5:	
						print("Thanks for this program:")
						exit()
			case 9: menu()
			case _:
					print("Ur Selection of operation is wrong, try again")
					menu()