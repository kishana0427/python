#filecountinfor1.py
import colorama
from colorama import Fore,Back
colorama.init(autoreset=True)
fname=input("Enter File Name:")
try:
	with open(fname,"r") as fp:
		nol=0
		nw=0
		nc=0
		for line in fp:
			print(line,end="")
			nol=nol+1
			nw=nw+len(line.split())
			nc=nc+len(line)
		print()
		print("-----------------------------------------------")
		print(Fore.RED+Back.YELLOW+"\nNumber of Lines=", nol)
		print(Fore.GREEN+Back.RED+"\nNumber of Words=", nw)
		print(Fore.YELLOW+Back.BLACK+"\nNumber of Characters=", nc)
		print("-----------------------------------------------")
except FileNotFoundError:
	print(Fore.YELLOW+Back.BLACK+"File does not exists:")
