#approach1.py
import threading,time
def  generate():
	print("Name of sub thread={}".format(threading.current_thread().name))
	n=int(input("\nEnter a number:"))
	if(n<=0):
		print("{} is invalid input:".format(n))
	else:
		print("-"*40)
		print("Numbers within:{}".format(n))
		print("-"*40)
		for i in range(1,n+1):
			print("Val of i={}".format(i))
			time.sleep(1)
		print("-"*40)

#main program
t=threading.Thread(target=generate)
print("Name of t=",t.name)
t.name="KVR" #setting the user-friendly Name to the sub-therad
t.start()
