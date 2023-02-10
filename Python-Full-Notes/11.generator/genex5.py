#genex5.py
def   decrgen(start,stop):
	if(stop>start):
		yield "stop value must be less than start value"
	while(start>=stop):
		yield start
		start=start-1

#main program
startval=int(input("Enter Start Value:"))
stopval=int(input("Enter Stop Value:"))
res=decrgen(startval,stopval)
for val in res:
	print(val)

