#atmdemo.py
from atmmenu import menu
from atmexcept import DepositError,WithdrawError,InSuffFundError
from atmoperations import *
while(True):
	menu()
	try:
		ch=int(input("Enter ur Choice:"))
		match ch:
			case 1:
				try:
					deposit()
				except ValueError:
					print("Don't try to deposit strs/symbols / alpha-numerics")
				except DepositError:
					print("Don't try to deposit -ve / zero values:")
			case 2:
				try:
					withdraw()
				except ValueError:
					print("Don't try to withdraw strs/symbols / alpha-numerics")
				except WithdrawError:
					print("Don't try to withdraw -ve / zero values:")
				except InSuffFundError:
					print("\nU don't have suff. Funds--read python notes:")
			case 3: balenq()
			case 4: 
				print("\nThanks for using this Application:")
				exit()
			case _:
				print("\nUr Selection of Operation is wrong:")
	except ValueError:
		print("\nDon't enter strs / symbols/alpha-numerics for ur choice:")