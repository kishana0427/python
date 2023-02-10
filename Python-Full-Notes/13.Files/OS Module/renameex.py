#renameex.py
import os
try:
	os.rename("C:\AMPT","C:\KVR")
	print("Folder Re-named--verify")
except FileNotFoundError:
	print("File name does not exists for Renaming")