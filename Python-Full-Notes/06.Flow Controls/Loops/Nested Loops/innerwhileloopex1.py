#innerwhileloopex1.py
i=1
while(i<=4):
	print("-------------------------------------------------")
	print("Val of i-outer while loop={}".format(i))
	print("-------------------------------------------------")
	j=10
	while(j<=12):
		print("\tVal of j-inner while loop={}".format(j))
		j=j+1
	print("\nInner while loop over")
	print("-------------------------------------------------")
	i=i+1
else:
	print("Outer while loop over")