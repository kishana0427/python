#genex2.py---define a generator which will generate 10 to 21 and 100 to 111
def  hyd(start,stop):        
	while(start<stop):
		yield start
		start=start+1

#main program
for val in hyd(10,21):
	print(val)
print("-----------------OR--------------------")
values=hyd(100,111)
while(True):
	try:
		print(next(values))
	except StopIteration:
		break


