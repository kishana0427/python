#syncex1.py---apply Locking mechanism--in OOPS
import threading,time
class MulTable:
	def __init__(self):
		self.l=threading.Lock()
	def table(self,n):
		self.l.acquire() # get the lock
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
		self.l.release() # release the lock
#main program
mt=MulTable()
t1=threading.Thread(target=mt.table,args=(9,) )
t2=threading.Thread(target=mt.table,args=(8,) )
t3=threading.Thread(target=mt.table,args=(23,) )
t4=threading.Thread(target=mt.table,args=(2,) )
t5=threading.Thread(target=mt.table,args=(-14,) )
'''t1.name="anand"
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