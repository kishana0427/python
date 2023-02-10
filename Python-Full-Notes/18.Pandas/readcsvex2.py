#readcsvex2.py
import csv  # here csv module contains reader() which returns an object of reader and whose object reads the csv file data in the form of records by eliminating delimiter comma (,)
try:
	with open("E:\KVR-PYTHON-11AM\PANDAS/NOTES\peoples.csv","r") as fp:
		csvp=csv.reader(fp)
		print("Type of csvp=",type(csvp)) # Type of csvp= <class '_csv.reader'>
		for people in csvp:
			for val in people:
				print("{}".format(val),end=" ")
			print()
except FileNotFoundError:
	print("CSV files does not exists:")


