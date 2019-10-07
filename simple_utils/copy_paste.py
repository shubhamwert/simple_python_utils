import pyperclip  as pp
import re

A=pp.paste()
B=A.split("\n")
C=""
for i in range(len(B)):
    if(B[i][0]!="/"):
        print(B[i])
        C=C+B[i]+"\n"
    else:
        continue

pp.copy(C)