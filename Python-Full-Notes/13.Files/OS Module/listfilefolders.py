#listfilefolders.py
import os
try:
	names=os.listdir("E:\KVR-PYTHON-11AM\FILES")
	for name in names:
		print("\t{}".format(name))
except FileNotFoundError:
	print("Folder does not exist to list files:")
