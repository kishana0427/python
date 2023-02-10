#sharesdemo.py
import shares
import time
import importlib
def disp(d):
	print("-"*50)
	print("\tShare Name\tValue")
	print("-"*50)
	for sn,sv in d.items():
		print("\t{}\t\t:{}".format(sn,sv))
	else:
		print("-"*50)
#main program
d=shares.sharesinfo()
disp(d)
time.sleep(15)
importlib.reload(shares)
d=shares.sharesinfo()
disp(d)
