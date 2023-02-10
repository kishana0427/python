#FileWriteEx2.py
d={10:"Python",20:"Django",30:"DS"}
fname=input("Enter the file name to write the data:")
with open(fname,"a") as fp:
	fp.writelines(str(d)+"\n")

print("Data written to the file--verify")

