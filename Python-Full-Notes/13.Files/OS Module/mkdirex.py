#mkdirex.py
import os
try:
	os.mkdir("C:\KVR\PYTHON")
	print("Folder created successfully--verify")
except FileExistsError:
	print("Folder already exists:")
