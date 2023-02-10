#FileReadEx3.py---read(no.of chars)
# tell()----->Gives Index of File Pointer in the file data area.
# seek(index)--->This function will re-set the file pointer  to the file data area
try:
	with open("addr1.info","r") as rp:
		print("--------------------------------------")
		print("Line:6-->Initial Pos of rp=",rp.tell())
		print("--------------------------------------")
		filedata=rp.read(5)
		print("File Data:",filedata)
		print("Line-10-->Now  Pos of rp=",rp.tell())
		filedata=rp.read(8)
		print("File Data:",filedata)
		print("Line-13->Now  Pos of rp=",rp.tell())
		filedata=rp.read()
		print("File Data:",filedata)
		print("Line-16->Now  Pos of rp=",rp.tell())
		print("-------------------------------------------------")
		rp.seek(0)
		print("Line:20-->Initial Pos of rp=",rp.tell())
		print("--------------------------------------")
		filedata=rp.read(13)
		print("File Data:",filedata)
		print("Line-24->Now  Pos of rp=",rp.tell())
		print("-------------------------------------------------")


except FileNotFoundError:
	print("File does not exists:")