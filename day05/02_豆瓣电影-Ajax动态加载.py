import requests
import json
import csv

url = "https://movie.douban.com/j/chart/top_list?"
params = {"type":"11",
          "interval_id":"100:90",
          "action":"",	
          "start":"0",
          "limit":"200"}

headers = {"User-Agent":"Mozilla5.0"}

res = requests.get(url,params=params,headers=headers)
res.encoding = "utf-8"
# 得到的json格式的数组[]
html = res.text
# 把json格式的数组转为python的列表
L = json.loads(html)

for film in L:
    score = film["rating"][0]
    name = film["title"]
    
    with open("豆瓣100.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name,score])
    













