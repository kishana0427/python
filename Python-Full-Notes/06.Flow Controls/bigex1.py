#bigex1.py
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
#logic for deciding big
if (a>b) and (a>c):
	print("big({},{},{})={}".format(a,b,c,a))
if(b>a) and (b>c):
	print("big({},{},{})={}".format(a,b,c,b))
if(c>a) and (c>b):
	print("big({},{},{})={}".format(a,b,c,c))
if(a==b) and (b==c):
	print("ALL VALUES ARE EQUAL")