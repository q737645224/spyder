import urllib.request
import urllib.parse

baseurl = "http://www.baidu.com/s?"
headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
key = input("请输入要搜索的内容:")
# urlencode编码,参数一定要是字典
d = {"wd":key}
d = urllib.parse.urlencode(d)
url = baseurl + d
# 构建请求对象
request = urllib.request.Request(url,headers=headers)
# 获取响应对象
response = urllib.request.urlopen(request)
# 获取内容
html = response.read().decode("utf-8")
print(html)






