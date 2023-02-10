#fibnoci.py
def     fibonociseries(n):
	if (n<=0):
		print("{} is inavlid input:".format(n))
	if(n==1):
		print("0")
	if(n==2):
		print("0")
		print("1")
	else:
			if(n==3):
				 n1=0
				 n2=1
				 n3=n1+n2
				 print("{}".format(n1))
				 print("{}".format(n2))
				 print("{}".format(n3))

			else:
				if(n>3):
					 n1=0
					 n2=1
					 n3=n1+n2
					 print("{}".format(n1))
					 print("{}".format(n2))
					 while(n3<=n):
						 print("{}".format(n3))
						 n1=n2
						 n2=n3
						 n3=n1+n2

#main program
n=int(input("Enter Number in which u want Fibonoci Series"))
fibonociseries(n)



