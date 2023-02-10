#makedirsex.py
import os
try:
	os.makedirs("C:\India\Hyd\Ameerpet\Python")
	print("Folders Hierarchy created..")
except FileExistsError:
	print("Folders Hierarchy alerady exists:")
except FileNotFoundError:
	print("Drive Name is Invalid:")
