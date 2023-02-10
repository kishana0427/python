#addition1.py
#Program for addition of two numbers by using Classes and objects
class Addition:
	def  getvalues(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
	
	def   findsum(self):
		self.getvalues()
		self.c=self.a+self.b
		self.dispvalues()

	def   dispvalues(self):
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("Sum={}".format(self.c))

#main program
ao=Addition()
ao.findsum()