#genex3.py---define a generator which will generate 10 to 21 and 100 to 111
def  hyd(start,stop,step):     
	if(start>stop):
		yield "start value must be less than stop value "
	while(start<stop):
		yield start
		start=start+step

#main program
startval=int(input("Enter Start Value:"))
stopval=int(input("Enter Stop Value:"))
stepval=int(input("Enter Step Value:"))
for val in hyd(startval,stopval,stepval):
	print(val)
print("--------------------OR----------------------")
values=hyd(startval,stopval,stepval)
while(True):
	try:
		print(next(values))
	except StopIteration:
		break

