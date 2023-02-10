#FileOpenEx4.py
try:
	with open("stud.data","r") as fp:
		print("file opened in read mode successfully")
		print("type of kvr=",type(fp))
		print("-------------------------------------------------")
		print("Name of File Mode =", fp.mode) # r
		print("is writeable?=", fp.writable()) # False
		print("is readable?=", fp.readable()) # True
		print("is file closed within with open() as ?=", fp.closed) # false
	
	print("\nis file closed out of with open() as indentation ?=", fp.closed) # True
except FileNotFoundError:
	print("File does not exists")
