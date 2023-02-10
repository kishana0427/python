#RegExpr22.py
#This program for searching ALL  except DIGITS
import re
mattab=re.finditer("\D", "kA b6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)
"""
E:\KVR-PYTHON-7AM\REG EXPR>py RegExpr22.py
--------------------------------------------------
Start Index:0  end Index=1  value=k
Start Index:1  end Index=2  value=A
Start Index:2  end Index=3  value=
Start Index:3  end Index=4  value=b
Start Index:5  end Index=6  value=&
Start Index:6  end Index=7  value=q
Start Index:7  end Index=8  value=P
Start Index:8  end Index=9  value=c
Start Index:9  end Index=10  value=H
Start Index:11  end Index=12  value=v
Start Index:12  end Index=13  value=@
Start Index:14  end Index=15  value=%
Start Index:15  end Index=16  value=L
Start Index:16  end Index=17  value=f
Start Index:17  end Index=18  value=P
Start Index:19  end Index=20  value=*
Start Index:20  end Index=21  value=
Start Index:22  end Index=23  value=K
Start Index:23  end Index=24  value=w
Start Index:24  end Index=25  value=R
--------------------------------------------------"""