#others3.py---Other Programmer attempting to access the data of other class object
from accountinfo3 import Account
ac=Account()  
print("------------------------------------------------")
print("Account Number=xxxxxxxx{}".format(ac.acno[-4:])) 
print("Account Holder Name={}".format(ac.cname))
#print("Account Balance={}".format(ac.bal))  can't access
#print("Account Pin={}".format(ac.pin))  can't acess
print("Account Branch Name={}".format(ac.bname))
print("------------------------------------------------")