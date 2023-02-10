#genex7.py
def  kvrrange(start,stop,step=0):
	if(step>0):
		if (start<stop):
			while(start<=stop):
				yield start
				start=start+step
		else:
			yield "start value must be less than stop value:"
	else:
		if(step<0):   
			if(start>stop): 
				while(start>=stop):
					yield start
					start=start+step
			else:
				yield "satrt value must be greater than stop"
		else:
			while(start<=stop):
				yield start
				start=start+1





