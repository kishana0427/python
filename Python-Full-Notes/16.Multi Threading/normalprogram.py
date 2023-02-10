#normalprogram.py
import threading,time
def  squares(lst):
	print("-"*40)
	print("squares() executed by=",threading.current_thread().name)
	for val in lst:
		print("sqrt({})={}".format(val,val**2))
		time.sleep(1)
	print("-"*40)

def  cubes(lst):
	print("-"*40)
	print("cubes() executed by=",threading.current_thread().name)
	for val in lst:
		print("cube({})={}".format(val,val**3))
		time.sleep(1)
	print("-"*40)
#main program
bt=time.time()
print("---------------------------------------------------------------------")
print("main program executed by=",threading.current_thread().name)
print("---------------------------------------------------------------------")
lst=[2,15,5,-6,34,9,10]
squares(lst)
cubes(lst)
print("---------------------------------------------------------------------")
et=time.time()
print("Exec time of Normal Program without sub threads=",(et-bt))
print("---------------------------------------------------------------------")