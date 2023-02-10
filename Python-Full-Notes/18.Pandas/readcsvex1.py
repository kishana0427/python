#readcsvex1.py
try:
	with open("E:\KVR-PYTHON-11AM\PANDAS/NOTES\peoples.csv","r") as fp:
		peoples=fp.readlines()
		for people in peoples:
			for val in people:
				print("{}".format(val),end="")
			print()
except FileNotFoundError:
	print("CSV files does not exists:")


