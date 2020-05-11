import requests
import pyperclip as pc

res = requests.get(pc.paste())
print(res.text[:250])
playfile=open(pc.paste(),'wb')

try:    
    res.raise_for_status()
    for chunk in res.iter_content(100000):
        playfile.write(chunk)

except Exception as exc:   
     print('There was a problem: %s' % (exc))
finally:
    playfile.close()


