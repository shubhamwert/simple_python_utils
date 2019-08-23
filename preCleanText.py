import re
import pyperclip

def remove_common_typos(p):
    space_regex=re.compile(r'\s+\s\w*')
    k=space_regex.search(p)

    print(' okay '+k.group(0))


remove_common_typos('hello world        prety')