#listprimes.py
print("Enter List of values separated by space:")
lst=[int(val) for val in input().split()]
print("Content of lst={}".format(lst))  #  [10,11,12,34,0,1,-4]
print("----------------------------------------------")
for n in lst:
	if(n<=1):
		print("{} is invalid input:".format(n))
	else:
		result=True
		for i in range(2,n):
			if(n%i==0):
				result=False
				break
		if(result):
			print("{} is prime:".format(n))
		else:
			print("{} is not prime:".format(n))

		


