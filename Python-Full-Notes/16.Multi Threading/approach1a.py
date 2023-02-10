#approach1a.py
import threading ,time
def  even(n):  # executed by sub therad
	print("-"*40)
	print("Name of sub thread={}".format(threading.current_thread().name))
	print("-"*40)
	for val in range(2,n+1,2):
		print("\t{}".format(val))
		time.sleep(1)
	else:
		print("-"*40)

#main program-----executed by main thread
#create sub thread
print("Name of main thread={}".format(threading.current_thread().name))
print("-"*40)
x=int(input("Enter Value of x:"))
t1=threading.Thread(target=even, args=(x,) )
print("Line-19--Number of active threads={}".format(threading.active_count()))
#dispatch the thread
t1.start()
print("Line-21--Number of active threads={}".format(threading.active_count()))
t1.join()
print("Line-23->Number of active threads={}".format(threading.active_count()))