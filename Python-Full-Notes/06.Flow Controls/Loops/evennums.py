#evennums.py
n=int(input("Enter number:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	print("-"*40)
	print("Even numbers within :{}".format(n))
	print("-"*40)
	i=2
	while(i<=n):
		print("val of i={}".format(i))
		print("-"*10)
		i=i+2
	else:
		print("*"*40)
