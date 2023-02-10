#others.py---Other Programmer attempting to access the data of other class object
from accountinfo import Account
ac=Account()
print("\nOBJECT data successfully Created:")
print("------------------------------------------------")
#print("Account Number={}".format(ac.acno))  can't acess
print("Account Holder Name={}".format(ac.cname))
#print("Account Balance={}".format(ac.bal)) can't access
#print("Account Pin={}".format(ac.pin)) can't access
print("Account Branch Name={}".format(ac.bname))
print("------------------------------------------------")