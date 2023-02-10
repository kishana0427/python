#filecountinfor.py
fname=input("Enter File Name:")
try:
	with open(fname,"r") as fp:
		nol=0
		nw=0
		nc=0
		for line in fp:
			print(line,end="")
			nol=nol+1
			nw=nw+len(line.split())
			nc=nc+len(line)
		print()
		print("-----------------------------------------------")
		print("\nNumber of Lines=", nol)
		print("\nNumber of Words=", nw)
		print("\nNumber of Characters=", nc)
		print("-----------------------------------------------")
except FileNotFoundError:
	print("File does not exists:")
