#primenumbers.py
def  prime(no):
	if(no<=1):
		print("{} is invalid input:".format(no))
	else:
		print("--------------------------------------------")
		print("Prime Number within:{}".format(no))
		print("--------------------------------------------")
		for n in range(2,no+1):
			res=True
			for i in range(2,n):
				if(n%i==0):
					res=False
					break
			if(res):
				print("\t{}".format(n))
		else:
			print("--------------------------------------------")

#main program
n=int(input("Enter Any Number, in which we want Prime numbers:"))
prime(n)
