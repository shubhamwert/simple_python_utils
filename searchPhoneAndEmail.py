import re
import pyperclip


    
phoneRegex=re.compile(r'''(
(\d{3}|\(\d{3}\))?    
(\s|-|\.)?
(\d{3})
(\s|-|\.)     
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @   
    [a-zA-Z0-9.-]+
    \.com 
)''',re.VERBOSE)


text=str(pyperclip.paste())
phones=phoneRegex.findall(text)
email=emailRegex.findall(text)
print(text)
print(phones)
print(email)

#test string::its shauir@ajnf.com reporting number 333-444-1111 and dfjans@ei.com