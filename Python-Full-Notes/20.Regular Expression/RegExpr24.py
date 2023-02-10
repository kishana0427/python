#RegExpr24.py
#This program for searching all special symbols
import re
mattab=re.finditer("\W", "kA b6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr24.py
--------------------------------------------------
Start Index:2  end Index=3  value=
Start Index:5  end Index=6  value=&
Start Index:12  end Index=13  value=@
Start Index:14  end Index=15  value=%
Start Index:19  end Index=20  value=*
Start Index:20  end Index=21  value=
--------------------------------------------------
"""

