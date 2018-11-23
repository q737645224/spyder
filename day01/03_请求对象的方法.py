import urllib.request

url = "http://www.baidu.com/"
headers = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"

# 1.构建请求对象
request = urllib.request.Request(url)
# 请求对象方法 add_header()
request.add_header("User-Agent",headers)
# 获取响应对象
response = urllib.request.urlopen(request)

# get_header()方法获取 User-Agent
print(request.get_header("User-agent"))















