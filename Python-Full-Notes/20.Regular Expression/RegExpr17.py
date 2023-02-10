#RegExpr17.py
#This program for searching  all  lower case  and upper case alphabets and digits
import re
mattab=re.finditer("[A-Za-z0-9]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr17.py
--------------------------------------------------
Start Index:0  end Index=1  value=k
Start Index:1  end Index=2  value=A
Start Index:2  end Index=3  value=b
Start Index:3  end Index=4  value=6
Start Index:5  end Index=6  value=q
Start Index:6  end Index=7  value=P
Start Index:7  end Index=8  value=c
Start Index:8  end Index=9  value=H
Start Index:9  end Index=10  value=7
Start Index:10  end Index=11  value=v
Start Index:12  end Index=13  value=8
Start Index:14  end Index=15  value=L
Start Index:15  end Index=16  value=f
Start Index:16  end Index=17  value=P
Start Index:17  end Index=18  value=3
Start Index:20  end Index=21  value=6
Start Index:21  end Index=22  value=K
Start Index:22  end Index=23  value=w
Start Index:23  end Index=24  value=R
-------------------------------------------
"""