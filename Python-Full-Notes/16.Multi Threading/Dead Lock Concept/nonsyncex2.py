#nonsyncex2.py---gives dead lock result--in Functional Programming
import threading,time
def table(n):
	print("Name of sub therad={}".format(threading.current_thread().name))
	if(n<=0):
		print("{} is InavlidInput:".format(n))
	else:
		print("-"*40)
		print("Mul Table for {}".format(n))
		print("-"*40)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
			time.sleep(1)
		print("-"*40)

#main program
t1=threading.Thread(target=table,args=(19,))
t2=threading.Thread(target=table,args=(18,) )
t3=threading.Thread(target=table,args=(9,) )
t4=threading.Thread(target=table,args=(8,) )
t5=threading.Thread(target=table,args=(-4,) )
''' t1.name="anand"
t2.name="sandeep"
t3.name="balu"
t4.name="rakesh"
t5.name="kiran" '''
#dispatch the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()