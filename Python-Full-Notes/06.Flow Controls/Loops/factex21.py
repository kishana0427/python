#factex21.py
n=int(input("Enter a number:"))
if(n<0):
	print("{} is invalid input:".format(n)) # n=4
else:
	  tn=n 
	  r=1
	  while(n>0):
		  r=r*n
		  n=n-1
	  else:
		  print("Factorial of {}={}".format(tn,r))