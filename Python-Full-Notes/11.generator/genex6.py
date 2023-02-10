#genex6.py
def   decrgen(start,stop,step):
	if(stop>start):
		yield "stop value must be less than start value"
	while(start>=stop):
		yield start
		start=start-step

#main program
startval=int(input("Enter Start Value:"))
stopval=int(input("Enter Stop Value:"))
stepval=int(input("Enter Step Value:"))
res=decrgen(startval,stopval,stepval)
for val in res:
	print(val)

