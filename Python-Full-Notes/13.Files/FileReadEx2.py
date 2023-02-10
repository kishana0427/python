#FileReadEx2.py
#This program copy the content of one file into another file
sfile=input("Enter Source File Name:")
try:
	with open(sfile,"r") as rp:
		dfile=input("Enter Destnation File:")
		with open(dfile,"a") as wp:
			sfiledata=rp.read()
			wp.write(sfiledata)
			print("File Copied--verify")

except FileNotFoundError:
	print("{}-->source File Does Not Exists:".format(sfile))
