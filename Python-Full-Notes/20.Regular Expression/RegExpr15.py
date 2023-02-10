#RegExpr15.py
#This program for searching  all  lower case  and upper case alphabets 
import re
mattab=re.finditer("[A-Za-z]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr15.py
--------------------------------------------------
Start Index:0  end Index=1  value=k
Start Index:1  end Index=2  value=A
Start Index:2  end Index=3  value=b
Start Index:5  end Index=6  value=q
Start Index:6  end Index=7  value=P
Start Index:7  end Index=8  value=c
Start Index:8  end Index=9  value=H
Start Index:10  end Index=11  value=v
Start Index:14  end Index=15  value=L
Start Index:15  end Index=16  value=f
Start Index:16  end Index=17  value=P
Start Index:21  end Index=22  value=K
Start Index:22  end Index=23  value=w
Start Index:23  end Index=24  value=R
--------------------------------------------------
"""