#primeex.py
n=int(input("Enter a number:"))
if(n<=1):
	print("{} is invalid input".format(n))
else:
	result=True
	for i in range(2,n):
		if(n%i==0):
			result=False
			break
	
	if(result):
		print("{} is PRIME Number:".format(n))
	else:
		print("{} is NOT PRIME Number:".format(n))

