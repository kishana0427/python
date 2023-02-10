#RegExpr9.py
#This program for searching  all upper  case alphabets
import re
mattab=re.finditer("[A-Z]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
Output
-------------------------------------------------- 
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr9.py
--------------------------------------------------
Start Index:1  end Index=2  value=A
Start Index:6  end Index=7  value=P
Start Index:8  end Index=9  value=H
Start Index:14  end Index=15  value=L
Start Index:16  end Index=17  value=P
Start Index:21  end Index=22  value=K
Start Index:23  end Index=24  value=R
--------------------------------------------------

"""