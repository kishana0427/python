#FileReadEx5.py---readlines()
try:
	with  open("addr1.info","r") as fp:
		filedatalines = fp.readlines()
		for fileline in filedatalines:
			print(fileline,end="")
		else:
			print("\n No. of lines=",len(filedatalines))
except FileNotFoundError:
	print("File  does not exists:")