#RegExpr23.py
#This program for searching all word char 
import re
mattab=re.finditer("\w", "kA b6&qPcH7v@8%LfP3* 6KwR")
print("-"*50)
for entry in mattab:
	print("Start Index:{}  end Index={}  value={}".format(entry.start(),entry.end(),entry.group()))
print("-"*50)

"""
:\KVR-PYTHON-7AM\REG EXPR>py RegExpr23.py
--------------------------------------------------
Start Index:0  end Index=1  value=k
Start Index:1  end Index=2  value=A
Start Index:3  end Index=4  value=b
Start Index:4  end Index=5  value=6
Start Index:6  end Index=7  value=q
Start Index:7  end Index=8  value=P
Start Index:8  end Index=9  value=c
Start Index:9  end Index=10  value=H
Start Index:10  end Index=11  value=7
Start Index:11  end Index=12  value=v
Start Index:13  end Index=14  value=8
Start Index:15  end Index=16  value=L
Start Index:16  end Index=17  value=f
Start Index:17  end Index=18  value=P
Start Index:18  end Index=19  value=3
Start Index:21  end Index=22  value=6
Start Index:22  end Index=23  value=K
Start Index:23  end Index=24  value=w
Start Index:24  end Index=25  value=R
--------------------------------------------------"""