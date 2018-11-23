import urllib.request

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}

# 1.构建请求对象
request = urllib.request.Request(url,headers=headers)
# 2.获取响应对象
response = urllib.request.urlopen(request)
# 3.获取响应对象内容
html = response.read().decode("utf-8")
# 获取响应码
print(response.getcode())
# 获取响应报头信息
print(response.info())


https://www.baidu.com/s?wd=%E7%BE%8E %E5%A5%B3








