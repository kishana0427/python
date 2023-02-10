#natnumssum.py
n=int(input("Enter How many Numbers:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	i=1
	s=0
	while(i<=n):
		s=s+i
		print("\t{}".format(i))
		i=i+1
	else:
		print("sum={}".format(s))