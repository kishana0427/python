#syncex2.py---gives Thread Safety result--in Functional Programming
#we apply Locking Mechanism
#We use a predefiend class "Lock" of threading 
import threading,time
def table(n):
	L.acquire()  # get the lock
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
	L.release()  # release  the lock
#main program
#create an object of Lock class
L=threading.Lock() #  here L is called Global variable
t1=threading.Thread(target=table,args=(19,) )
t5=threading.Thread(target=table,args=(-4,) )
t2=threading.Thread(target=table,args=(18,) )
t3=threading.Thread(target=table,args=(9,) )
t4=threading.Thread(target=table,args=(8,) )
'''t1.name="anand"
t2.name="sandeep"
t3.name="balu"
t4.name="rakesh"
t5.name="kiran" '''
#dispatch the threads
t1.start()
t5.start()
t2.start()
t3.start()
t4.start()
