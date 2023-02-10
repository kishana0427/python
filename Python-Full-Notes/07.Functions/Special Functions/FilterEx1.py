#FilterEx1.py
def  even(n):
	if(n%2==0):
		return True
	else:
		return False

def  odd(n):
	if(n%2!=0):
		return True
	else:
		return False

#main program
lst=[23,21,46,48,27,78,71,23]
filtobj1=filter(even,lst)
print("-------------------------------------------")
print("type filtobj=",type(filtobj1)) # type filtobj1= <class 'filter'>
print(filtobj1) # <filter object at 0x0000013C11C5F100>
print("-------------------------------------------")
print("Given Elements={}".format(lst))
evenlst=list(filtobj1)
print("Even Elements={}".format(evenlst))
filtobj2=filter(odd,lst)
oddlst=tuple(filtobj2)
print("Odd Elements={}".format(oddlst))

