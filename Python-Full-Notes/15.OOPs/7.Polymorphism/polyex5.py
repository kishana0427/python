#ployex5.py
class Rossum:
	def  getsubject(self):
		print("Rossum Developed Python:")
class Gosling:
	def getsubject(self):
		print("Gosling developed Java:")
class Ritche:
	def getsubject(self):
		print("Ritche developed C")

class KVR(Rossum,Gosling,Ritche):
	def  getsubject(self):  # overridden method
		print("KVR teaches C,JAVA and PYTHON")
		print("------------------------------------------")
		Gosling.getsubject(self)
		Ritche.getsubject(self)
		Rossum.getsubject(self)
#main program
k=KVR()
k.getsubject()

