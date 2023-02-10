#innerforloopex1.py
for i in range(1,5):
	print("-------------------------------------------------")
	print("Val of i-outer for loop={}".format(i))
	print("-------------------------------------------------")
	for j in range(10,13):
		print("\tVal of j-inner for loop={}".format(j))
	print("\nInner for loop over")
	print("-------------------------------------------------")
else:
	print("Outer for loop over")