#operation.py----file name and acts as module name
from kvr import KvDivisionError
def   divop(a,b):
	if(b==0):
		raise KvDivisionError   # hiting / generating  the exception
	else:
		c=a/b
		return c
	
