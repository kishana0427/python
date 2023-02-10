#syncex3.py---apply Locking mechanism--in OOPS
import threading,time
class MulTable(threading.Thread):
	def  setvalue(self,n):
		self.n=n
	def run(self):
		L.acquire()
		print("Name of sub therad={}".format(threading.current_thread().name))
		if(self.n<=0):
			print("{} is InavlidInput:".format(self.n))
		else:
			print("-"*40)
			print("Mul Table for {}".format(self.n))
			print("-"*40)
			for i in range(1,11):
				print("\t{} x {} = {}".format(self.n,i,self.n*i))
				time.sleep(1)
			print("-"*40)
		L.release() # release the lock
#main program
L=threading.Lock()
t1=MulTable()
t1.setvalue(19)
t2=MulTable()
t2.setvalue(8)
t3=MulTable()
t3.setvalue(-5)
t4=MulTable()
t4.setvalue(34)
#dispatch the threads
t1.start()
t2.start()
t3.start()
t4.start()
