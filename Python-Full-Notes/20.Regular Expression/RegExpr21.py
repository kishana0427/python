#RegExpr21.py
#This program for searching ALL DIGITS
import re
mattab=re.finditer("\d", "kA b6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr21.py
--------------------------------------------------
Start Index:4  end Index=5  value=6
Start Index:10  end Index=11  value=7
Start Index:13  end Index=14  value=8
Start Index:18  end Index=19  value=3
Start Index:21  end Index=22  value=6
----------------------------------------------------------------------------------------------------

"""





























