#removedirsex.py
import os
try:
	os.removedirs("E:\KVR-PYTHON-11AM\FILES")
	print("Folder Removed--cerify")
except FileNotFoundError:
	print("Folder does not exists/ Invalid Drive Name:")
except OSError:
	print("Folder Must be empty:")
