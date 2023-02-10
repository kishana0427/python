#FileOpenEx3.py
try:
	fp=open("stud1.data","x")
	print("\nFile opened in write mode Exclusively:")
	print("type of fp=",type(fp))
	print("-------------------------------------------------")
	print("Name of File Mode =", fp.mode) # w 
	print("is writeable?=", fp.writable()) # True
	print("is readable?=", fp.readable()) # False
	print("is file closed?=", fp.closed) # false
except FileExistsError:
	print("Already this file exist--we can't re-create again with 'x' mode :")
