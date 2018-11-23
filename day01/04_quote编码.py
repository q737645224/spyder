import urllib.request
import urllib.parse

headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
url = "http://www.baidu.com/s?wd="
key = input("请输入要搜索的内容:")
# 编码,拼接URL
key = urllib.parse.quote(key)
fullurl = url + key
# 构建请求对象
request = urllib.request.Request(fullurl,headers=headers)
# 获取响应对象
response = urllib.request.urlopen(request)
# read().decode()
html = response.read().decode("utf-8")
print(html)



















