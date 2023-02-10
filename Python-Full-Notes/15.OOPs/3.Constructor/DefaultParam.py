#DefaultParam.py
class Test:
	def  __init__(self,a=100,b=200):
		self.a=a
		self.b=b
		print("\t{}\t{}".format(self.a,self.b))


#main program
t1=Test()
t2=Test(10)
t3=Test(10,20)

"""
===================================================
=>In a class of Python we can't define both Default and Parameterized constructors bcoz PVM can remember only latest defined constructor even we define multiple types of constructors (bcoz PVM is an Interpreter) . To solve this issue , and to fullfill the functionality of Both default and parameterized constructors we must define single parameterized constructor( To Fullfill parameterized constructor Functionality ) with default Params (To Full fill default constructor Functionality ).
====================================X========================"""

