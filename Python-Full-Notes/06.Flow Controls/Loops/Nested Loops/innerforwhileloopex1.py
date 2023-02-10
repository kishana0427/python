#innerforwhileloopex1.py
for i in range(5,0,-1):
	print("-------------------------------------------------")
	print("Val of i-outer for loop={}".format(i))
	print("-------------------------------------------------")
	j=12
	while(j>=10):
		print("\tVal of j-inner while loop={}".format(j))
		j=j-1
	print("\nInner while loop over")
	print("-------------------------------------------------")
else:
	print("Outer for loop over")