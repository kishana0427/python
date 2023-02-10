#studunpick.py
#This Programs gets student record from file by using un-pickling concept by with load() of pickle
import colorama
from colorama import Back,Fore
colorama.init(autoreset=True)
import pickle
try:
	with  open("stud.info","rb") as fp:
		print("-"*60)
		print("\t"+Fore.RED+Back.YELLOW+"\tS t u d e n t  D e t a i l s")
		print("-"*60)
		print("\t"+Fore.RED+Back.YELLOW+"\tStudNo\t\tStudName\t\tStud Marks")
		print("-"*60)
		while(True):
			try:
				record=pickle.load(fp)
				for val in record:
					print(Fore.YELLOW+Back.BLACK+"\t\t{}".format(val),end="   ")
				print()
			except EOFError:
				print("-"*60)
				break
except FileNotFoundError:
	print("File does not exists:")
