#globalsfunex1.py
a=10
b=20
c=30
d=40   # here 'a' 'b' 'c' and 'd' are called global variables.
def   operation():
	print("--------------------------------")
	global c,d
	c=c+1   # c=31
	d=d+1  # d=41
	a=100
	b=200  # here 'a' and 'b' are called Local Variables.
	e=a+b+c+d+globals()['a']+globals()['b']
	print("result=",e)
	print("-------------OR-------------------")
	e=a+b+c+d+globals().get('a')+globals().get('b')
	print("result=",e)
	print("-------------OR-------------------")
	x=globals()  # here x is of type <class,'dict'>
	e=a+b+c+d+x.get('a')+x.get('b')
	print("result=",e)
	print("-------------OR-------------------")
	e=a+b+c+d+x['a']+x['b']
	print("result=",e)
			
#main program
operation()
