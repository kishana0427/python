#FileReadEx4.py---readline()
try:
	with  open("addr1.info","r") as fp:
		line=fp.readline()
		while line:
			print(line,end="")
			line=fp.readline()
except FileNotFoundError:
	print("File  does not exists:")