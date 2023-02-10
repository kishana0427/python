#natnumsums.py
n=int(input("Enter How many Numbers:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-"*50)
	print("\tNat Nums\tSquares\t\tCubues ")
	print("-"*50)
	i=1
	s,ss,cs=0,0,0
	while(i<=n):
		s=s+i
		ss=ss+i**2
		cs=cs+i**3
		print("\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
		i=i+1
	else:
		print("-------------------------------------------")
		print("\t{}\t\t{}\t\t{}".format(s,ss,cs))
		print("-------------------------------------------")