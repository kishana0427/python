#addition4.py
def   addop():
	#taking input
	m,n=float(input("Enter First value:")), float(input("Enter Second Value:"))
	#process
	k=m+n
	#return the result
	return m,n,k

#main program
m,n,k=addop()
print("sum({},{})={}".format(m,n,k))
print("---------------OR-----------------------")
kvr=addop()  # here kvr is variable / object of type <class,'tuple'>
print("Sum({},{})={}".format(kvr[0],kvr[1],kvr[2]))