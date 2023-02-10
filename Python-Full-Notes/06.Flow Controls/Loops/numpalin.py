#numpalin.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	tn=n
	r=0
	while(n>0):
		d=n%10
		r=r*10+d
		n=n//10
	else:
		if(tn==r):
			print("Given Number is Palindrome")
		else:
			print("Given Number is Not Palindrome")


	
