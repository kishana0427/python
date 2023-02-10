#matchcaseex1.py
wkno=int(input("Enter Week Number:"))
match wkno:
	case 1:
			print("Its MONDAY")
	case 2:
			print("Its TUESDAY")
	case 3:
			print("Its WEDNESDAY")
	case 4:
			print("Its THURSDAY")
	case 5:
			print("Its FRIDAY")
	case 6:
			print("Its SATDAY")
	case 7:
			print("Its SUNDAY")
	case _:
			print("Its not a week number--learn weeks  ")
print("Program over")
	
	
			