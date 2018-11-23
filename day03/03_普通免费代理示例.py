import requests

url = "http://www.taobao.com/"
proxies = {"HTTP":"222.221.11.119:3128"}
headers = {"User-Agent":"Mozilla5.0/"}

res = requests.get(url,proxies=proxies,headers=headers)
res.encoding = "utf-8"
print(res.text)





