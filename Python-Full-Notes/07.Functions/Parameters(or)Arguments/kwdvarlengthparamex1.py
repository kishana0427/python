#kwdvarlengthparamex1.py
def  studhobbies( **k  ):
	print("------------------------")
	for key,val in k.items():
		print("\t{}-->{}".format(key,val))
	print("------------------------")

#main program
studhobbies(stno=10,name="Off-Pavan",habit1="Eat Chewing Gum")
studhobbies(sno=20,sname="Rossum",Invent1="python2.x",invent2="Python3.x")
studhobbies(no=20,sname="Kiran",habit="Sleep")
studhobbies(sname="KVR",habit="Teaching")