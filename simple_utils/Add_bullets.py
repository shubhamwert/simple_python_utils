import pyperclip
import sys
text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='*'+lines[i]


text='\n'.join(lines)
print(text)
pyperclip.copy(text)
