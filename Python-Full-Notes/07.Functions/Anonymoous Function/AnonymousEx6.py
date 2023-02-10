#AnonymousEx6.py
decide = lambda n: "Even " if (n%2==0 ) else "Odd"
#main program
print("Enter List of values separated by space:")
nums=[int(x) for x in input().split()]
for val in nums:
	print("Number({})={}".format(val, decide(val)))
