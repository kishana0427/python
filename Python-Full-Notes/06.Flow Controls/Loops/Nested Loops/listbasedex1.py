#listbasedex1.py
n=int(input("Enter How many number sum and avg u want to find:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	l=list()    # or   l=[ ]
	for i in range(1,n+1):
		val=float(input("Enter {} value:".format(i)))
		l.append(val)
	else:
		print("-----------------------------------")
		print("Content of l={}".format(l)) # [10.0, 15.0, 8.0, 2.0, 6.0]
		print("-----------------------------------")
		s=0
		for val in l:
			s=s+val
		else:
			print("--------------------------")
			print("Sum={}".format(s))
			print("Avg={}".format(s/len(l)))
			print("--------------------------")



