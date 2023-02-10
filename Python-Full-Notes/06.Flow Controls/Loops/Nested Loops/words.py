#words.py
n=input("Enter a number:")
print("val of n=",n)
i=0
while(i<len(n)):  # 3450
	d=n[i]
	match int(d):
			case 0:  print("Zero",end=" ")
			case 1:  print("One",end=" ")
			case 2:  print("Two",end=" ")
			case 3:  print("Three",end=" ")
			case 4:  print("Four",end=" ")
			case 5:  print("Five",end=" ")
			case 6:  print("Six",end=" ")
			case 7:  print("Seven",end=" ")
			case 8:  print("Eight",end=" ")
			case 9:  print("Nine",end=" ") 
	i=i+1

