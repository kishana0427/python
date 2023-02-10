#multables.py
print("Enter List of values separated by space:")
lst=[int(val) for val in input().split()]
print("Content of lst={}".format(lst))
print("-"*50)
for n in lst:
	if(n<=0):
		print("{} is invalid input:".format(n))
	else:
		print("Mul table for {}".format(n))
		print("-"*40)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
		print("-"*40)

