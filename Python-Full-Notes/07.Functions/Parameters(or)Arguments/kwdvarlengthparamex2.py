#kwdvarlengthparamex2.py
def  findtotalmarks(sno,sname,cls,cnt="India",**submarks) :
	print("-"*40)
	print("\tStudent Information:")
	print("-"*40)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{} ".format(sname))
	print("\tClass : {}".format(cls))
	print("\tCountry:{}".format(cnt))
	print("-"*40)
	print("\tSubjects\tMarks")
	print("-"*40)
	tm=0
	for subject,marks in submarks.items():
		print("\t{}\t\t{}".format(subject,marks))
		tm=tm+marks
	else:
		print("-"*40)
		print("\tTotal Marks:{}".format(tm))
		print("-"*40)

#main program
findtotalmarks(10,"Pavan","X",Hindi=90,maths=88,sci=77,soc=66,eng=66)
findtotalmarks(20,"Ajay","XII",phy=59,che=58,maths=73)
findtotalmarks(30,"Srinivas","B.Tech",AI=66,ML=55,DL=66,Python=77,DS=44)
findtotalmarks(40,"Rossum","Research",cnt="NL",python=99,)



