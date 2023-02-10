#big.py
a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
if(a==b):
    print("BOTH VALUE ARE EQUAL")
else:
    if(a>b):
        print("big({},{})={}".format(a,b,a))
    else:
        print("big({},{})={}".format(a,b,b))