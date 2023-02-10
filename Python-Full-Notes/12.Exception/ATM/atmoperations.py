#atmoperations.py
from atmexcept import DepositError,WithdrawError,InSuffFundError
bal=500.00 # global Variable
def   deposit():
	damt=float(input("\nEnter how much amount u want to deposit:"))#ValueError
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("\nUr Account xxxxxx123 credited with INR:{}".format(damt))
		print("Now Ur Current Balanace:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("\nEnter how much amount u want to withdraw:"))#ValueError
	if(wamt<=0):
		raise  WithdrawError
	else:
		if(wamt+500>bal):
			raise InSuffFundError
		else:
			bal=bal-wamt
			print("\nUr Account xxxxxx123 debited  with INR:{}".format(wamt))
			print("Now Ur Current Balanace:{}".format(bal))

def  balenq():
		print("Ur Current Balanace:{}".format(bal))