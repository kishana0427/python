#globalkwdex1.py
a=10
b=20   # here 'a' and 'b' are called global variables
def   operation1():
	d=a+b+c  # here 'd' is called local Variable
	print("sum={}".format(d))
def   operation2():
	d=a-b-c   # here 'd' is called local Variable
	print("sub={}".format(d))

#main program
c=30  # global variable
operation1()
operation2()