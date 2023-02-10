#MultipleLines.py
#This program writes multiple lines of text to the file.
with open("hyderabad.info","a") as fp:
	print("Enter Multiple Lines of text and press('quit') to stop:\n")
	while True:
		mldata=input()
		if(mldata!='quit'):
			fp.write(mldata+"\n")
		else:
			break
	print("\nData written to the file--verify")