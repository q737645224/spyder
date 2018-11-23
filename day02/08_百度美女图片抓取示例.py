import requests

url = "http://08.imgmini.eastday.com/mobile/20180723/987b2a935887efed40eda8e0e7cd4c13_wmk.jpeg"
headers = {"User-Agent":"Mozilla5.0/"}

response = requests.get(url,headers=headers)
# content属性获取响应内容(bytes)
data = response.content

with open("赵丽颖.jpg","wb") as f:
    f.write(data)





