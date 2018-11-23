import requests

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla5.0/"}
# 发请求获响应对象
response = requests.get(url,headers=headers)
response.encoding = "utf-8"
# 获取响应内容,text返回字符串
#print(response.text)
# content返回bytes
#print(response.content)
print(response.status_code)


















