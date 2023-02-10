#verifier.py---file name and acts as module name
from logindet import LoginError
from multable import table
def   loginprocess(un,pw):
	if ((un=="kvr") and   (pw=="python")):
		n=int(input("Enter a number for generating mul table:"))
		table(n)
	else:
		raise LoginError    # here LoginError is a programmer-define exception class
									# hitting th exception by using raise kwd.

