#globalkwdex3.py
a=10
b=20   # here 'a' and 'b' are called global variable.
def  modifyvalues():
	global a,b  # refering global Variable Values 'a' and 'b'
	a=a+1
	b=b+1
	print("val of a in modifyvalues()={}".format(a))
	print("val of b in modifyvalues()={}".format(b))

#main program
print("Val of a before modifyvalues()={}".format(a))
print("Val of b before modifyvalues()={}".format(b))
modifyvalues()
print("Val of a after modifyvalues()={}".format(a))
print("Val of b after modifyvalues()={}".format(b))