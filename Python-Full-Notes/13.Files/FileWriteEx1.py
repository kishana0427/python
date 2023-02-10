#FileWriteEx1.py
fname=input("Enter the file name to write the data:")
with  open(fname,"a") as fp:
	fp.write("Guido Van Rossum\n")
	fp.write("3-4,Red Sea Side\n")
	fp.write("Python software Foundation\n")
	fp.write("Nether Lands\n")
	fp.write(str(500013)+"\n")

print("Data Written to the file successfully--plz verify")
