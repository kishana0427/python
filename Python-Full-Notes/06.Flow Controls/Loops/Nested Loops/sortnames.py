#sortnames.py
n=int(input("Enter How many names u have:"))
if(n<=0):
	print("{} invalid input:".format(n))
else:
	l=list()
	print("-----------------------------------------")
	print("Enter {} names".format(n))
	print("-----------------------------------------")
	for i in range(1,n+1):
		name=input()
		l.append(name)
	else:
		print("-----------------------------------------")
		print("Given Names:")
		print("-----------------------------------------")
		for name in l:
			print(name)
		print("-----------------------------------------")
		l.sort()
		print("Sorted  Names--ASC order:")
		print("-----------------------------------------")
		for name in l:
			print(name)
		print("-----------------------------------------")
		l=l[::-1]
		print("Sorted  Names--DESC order:")
		print("-----------------------------------------")
		for name in l:
			print(name)
		print("-----------------------------------------")



