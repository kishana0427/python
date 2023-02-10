#RegExpr14.py
#This program for searching  all  except lower case alphabets and digits
import re
mattab=re.finditer("[^a-z0-9]", "kAb6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)


""""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr14.py
--------------------------------------------------
Start Index:1  end Index=2  value=A
Start Index:4  end Index=5  value=&
Start Index:6  end Index=7  value=P
Start Index:8  end Index=9  value=H
Start Index:11  end Index=12  value=@
Start Index:13  end Index=14  value=%
Start Index:14  end Index=15  value=L
Start Index:16  end Index=17  value=P
Start Index:18  end Index=19  value=*
Start Index:19  end Index=20  value=
Start Index:21  end Index=22  value=K
Start Index:23  end Index=24  value=R
--------------------------------------------------
"""