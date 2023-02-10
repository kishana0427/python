#threadsprogram.py
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
#create two sub threads created by main thread
t1=threading.Thread(target=squares, args=(lst,) )
t2=threading.Thread(target=cubes, args=(lst,) )
t1.start()
t2.start()
print("Number active Threads---linw-29=",threading.active_count()) # 3 (1+2)
t1.join()
t2.join()
print("Number active Threads---linw-32=",threading.active_count()) # 1
print("---------------------------------------------------------------------")
et=time.time()
print("Exec time of Normal Program without sub threads=",(et-bt))
print("---------------------------------------------------------------------")
