#mapex1.py
def  square(n):
	return (n**2)
def sqrtfun(n):
	return (n**0.5)

# main program
print("Enter List of Values separated Space:")
lst=[int(x) for x in input().split()]
mapobj1=map(square,lst)
print("type of mapobj1=",type(mapobj1)) # type of mapobj1= <class 'map'>
sqlst=tuple(mapobj1)
sqrtlist=list(map(sqrtfun,lst))
print("-------------------------------------------------")
print("Given Elements={}".format(lst))
print("Square list={}".format(sqlst))
print("Square Root list")
for sqrtval in sqrtlist:
	print("\t{}".format(round(sqrtval,2)))