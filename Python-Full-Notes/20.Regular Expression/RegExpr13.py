#RegExpr13.py
#This program for searching  all  lower case alphabets and digits
import re
mattab=re.finditer("[a-z0-9]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
Output
-------------------------------------------------- 
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr13.py
--------------------------------------------------
Start Index:0  end Index=1  value=k
Start Index:2  end Index=3  value=b
Start Index:3  end Index=4  value=6
Start Index:5  end Index=6  value=q
Start Index:7  end Index=8  value=c
Start Index:9  end Index=10  value=7
Start Index:10  end Index=11  value=v
Start Index:12  end Index=13  value=8
Start Index:15  end Index=16  value=f
Start Index:17  end Index=18  value=3
Start Index:20  end Index=21  value=6
Start Index:22  end Index=23  value=w
--------------------------------------------------

"""
