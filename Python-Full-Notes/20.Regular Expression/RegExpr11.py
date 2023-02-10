#RegExpr11.py
#This program for searching  all  digits
import re
mattab=re.finditer("[0-9]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
Output
-------------------------------------------------- 
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr11.py
--------------------------------------------------
Start Index:3  end Index=4  value=6
Start Index:9  end Index=10  value=7
Start Index:12  end Index=13  value=8
Start Index:17  end Index=18  value=3
Start Index:20  end Index=21  value=6
--------------------------------------------------
"""