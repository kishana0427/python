#aop.py--file name and treated as module name
def  readvalues(op):
	a=float(input("Enter First Value for {}".format(op)))
	b=float(input("Enter Second Value for {}".format(op)))
	return a,b
def   addop():
	k,v=readvalues("Addition:")
	print("sum({},{})={}".format(k,v,k+v))
def   subop():
	a,b=readvalues("Substraction:")
	print("sub({},{})={}".format(a,b,a-b))
def   mulop():
	m=readvalues("Multiplication:")
	print("mul({},{})={}".format(m[0],m[1],m[0]*m[1]))
def   divop():
	a,b=readvalues("Division:")
	print("div({},{})={}".format(a,b,a/b))
	print("floor div({},{})={}".format(a,b,a//b))
def   modop():
	a,b=readvalues("Modulas:")
	print("mod({},{})={}".format(a,b,a%b))
def   expoop():
	a=float(input("Enter Base:"))
	b=float(input("Enter Power:"))
	print("pow({},{})={}".format(a,b,a**b))
