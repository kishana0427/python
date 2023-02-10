#readpandacsv.py
import pandas as pd1 # here pandas module contains read_csv()  and it can read any data present csv file it returns all the records in the object of DataFrame
csvrecs=pd1.read_csv("C:\KVR-HYD\peoples.csv")
print(csvrecs,type(csvrecs))
