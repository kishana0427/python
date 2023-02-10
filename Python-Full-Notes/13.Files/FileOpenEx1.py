#FileOpenEx1.py
try:
	fp=open("stud.data","r+")
	print("file opened in read mode successfully")
	print("type of kvr=",type(fp))
	print("-------------------------------------------------")
	print("Name of File Mode =", fp.mode) # r
	print("is writeable?=", fp.writable()) # False
	print("is readable?=", fp.readable()) # True
	print("is file closed?=", fp.closed) # false
except FileNotFoundError:
	print("File does not exists")
finally:
	print("\ni am from finally block")
	fp.close()
	print("File Closed:")
	print("is file closed?=", fp.closed) # True
