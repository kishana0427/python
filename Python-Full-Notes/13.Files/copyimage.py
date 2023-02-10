#copyimage.py
try:
	with open("E:\KVR-FULLSTACK-DS\jpstudent.png","rb") as rp:
		with open("pythonjavastud.png","wb") as wp:
			filedata=rp.read()
			wp.write(filedata)
			print("\nIamge Copied!--Verify")
except FileNotFoundError:
	print("File does not exists:")