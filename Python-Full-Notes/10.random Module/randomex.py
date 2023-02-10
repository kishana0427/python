#randomex.py
import random
lst=[]
for i in range(1,6):
	lst.append("%0.2f" %random.random())
print("---------------------------------------")
print("Content of lst={}".format(lst))
