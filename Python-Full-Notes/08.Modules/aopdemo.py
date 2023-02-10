#aopdemo.py
from menuop import menuop
from aop import addop,subop,mulop,divop,modop,expoop
while(True):
	menuop()
	ch=int(input("Enter Ur Choice:"))
	match ch:
		case 1:addop()
		case 2:subop()
		case 3:mulop()
		case 4:divop()
		case 5: modop()
		case 6:expoop()
		case 7:
			print("Thanks for using the Program!")
			exit()
		case _:
			print("Ur Selection of Choice is wrong-Try again")