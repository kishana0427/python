#RegExpr18.py
#This program for searching  all  special symbols
import re
mattab=re.finditer("[^A-Za-z0-9]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr18.py
--------------------------------------------------
Start Index:4  end Index=5  value=&
Start Index:11  end Index=12  value=@
Start Index:13  end Index=14  value=%
Start Index:18  end Index=19  value=*
Start Index:19  end Index=20  value=
--------------------------------------------------
"""