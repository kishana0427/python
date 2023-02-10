#AnonymousEx1.py
def sumop(a,b):  # Normal Function definition
	c=a+b
	return c

addop=lambda a,b:a+b  # Anonymous Function Definiton

#main program
res1=sumop(float(input("Enter First Value:")), float(input("Enter Second Value:")))
print("Type of sumop=",type(sumop)) # Type of sumop= <class 'function'>
print("sum=",res1)
print("------------------OR--------------------")
print("Type of addop=",type(addop)) # Type of addop= <class 'function'>
n=float(input("Enter First Value:"))
m=float(input("Enter Second Value:"))
res2=addop(n,m)
print("sum=",res2)
print("-------------OR-----------------------")
print("sum={}".format(addop(float(input("Enter First Value:")), float(input("Enter Second Value:")) )))