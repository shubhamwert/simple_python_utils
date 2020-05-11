import requests,bs4
res=requests.get("http://google,com")
res.raise_for_status()
beautyfulres=bs4.BeautifulSoup(res)
