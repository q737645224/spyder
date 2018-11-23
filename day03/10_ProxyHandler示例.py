import urllib.request

url = "http://www.baidu.com/"
proxy = {"HTTP":"183.62.196.10:3128"}
# 1.创建Handler
proxy_handler = urllib.request.ProxyHandler(proxy)
# 2.创建自定义opener
opener = urllib.request.build_opener(proxy_handler)
# 3.利用open方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))








