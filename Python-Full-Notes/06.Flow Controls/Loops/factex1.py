#factex1.py
n=int(input("Enter a number:"))
if(n<0):
	print("{} is invalid input:".format(n))
else:
	i=1
	r=1
	while(i<=n):
		r=r*i
		i=i+1
	else:
		print("Factorial of {}={}".format(n,r))