#rmdirex.py
import os
try:
	os.rmdir("C:\India\Hyd\Ameerpet\Python")
	print("Folder Removed--cerify")
except FileNotFoundError:
	print("Folder does not exists:")
except OSError:
	print("Folder Must be empty:")
