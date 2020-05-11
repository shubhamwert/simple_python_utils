import webbrowser
import pyperclip
import sys

#check if there are arguments in command shell

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])

#else check clipboard
else:
    address=" ".join(pyperclip.paste())
webbrowser.open('https://www.google.com/maps/place/' + address)


