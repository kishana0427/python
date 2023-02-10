#FileReadEx1.py------>read()
fname=input("Enter File Name to read its content:")
try:
	with open(fname,"r") as fp:
		filedata=fp.read()
		print("------------------------------")
		print("file Data")
		print("------------------------------")
		print(filedata)
		print("------------------------------")
except FileNotFoundError:
	print("\n{} does not exists:".format(fname))