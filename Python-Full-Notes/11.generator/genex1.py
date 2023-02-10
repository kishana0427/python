#genex1.py--define a generator, which will generate 0 to n-1 values.
def   kvr(n):
	i=0
	while(i<n):
		yield i
		i=i+1

#main program
res=kvr(11)
while(True):
	try:
		print(next(res))
	except StopIteration:
		break
print("-----------------OR------------------------")
for x in kvr(11):
	print(x)
