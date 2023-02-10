#multable.py
def  table(n):
	if(n<=0):
		print("{} is invalid input:".format(n))
	else:
		print("----------------------------------------------")
		print("Mul table for :{}".format(n))
		print("----------------------------------------------")
		for i in range(1,11):
			print("\t{}x{}={}".format(n,i,n*i))
		print("----------------------------------------------")
#main program
n=int(input("Enter any number:"))
table(n)
