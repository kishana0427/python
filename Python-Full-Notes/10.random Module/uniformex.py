#uniformex.py
import random
lst=[]
for i in range(1,6):
	lst.append(float("%0.2f" %random.uniform(10,15.5)))
print("---------------------------------------")
print("Content of lst={}".format(lst))
