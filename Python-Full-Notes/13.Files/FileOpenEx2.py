#FileOpenEx2.py
fp=open("stud.data","w+")
print("\nFile opened in write mode successfully:")
print("type of fp=",type(fp))
print("-------------------------------------------------")
print("Name of File Mode =", fp.mode) # w 
print("is writeable?=", fp.writable()) # True
print("is readable?=", fp.readable()) # False
print("is file closed?=", fp.closed) # false
