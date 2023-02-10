#RegExpr19.py
#This program for searching  all  space character only
import re
mattab=re.finditer("\s", "kA b6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""" OUTPUT
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr19.py
--------------------------------------------------
Start Index:2  end Index=3  value=
Start Index:20  end Index=21  value=
--------------------------------------------------  """