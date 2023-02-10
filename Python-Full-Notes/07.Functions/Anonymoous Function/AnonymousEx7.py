#AnonymousEx7.py
decide = lambda n: n%2==0 
#main program
print("Enter List of values separated by space:")
nums=[int(x) for x in input().split()]
for val in nums:
	print("iseven({})={}".format(val, decide(val)))
