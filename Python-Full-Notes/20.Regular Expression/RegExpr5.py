#RegExpr5.py
#This program for searching either 'a' or 'b' or 'c'
import re
mattab=re.finditer("[abc]", "kAb6&qPch7v@8%LfP3* 6Kwr")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
Output
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr5.py
--------------------------------------------------
Start Index:2  end Index=3  value=b
Start Index:7  end Index=8  value=c
--------------------------------------------------   """