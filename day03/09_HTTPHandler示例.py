import urllib.request

url = "http://www.baidu.com/"
# 1.创建HTTPHandler处理器对象
http_hander = urllib.request.HTTPHandler()
# 2.创建自定义的opener对象
opener = urllib.request.build_opener(http_hander)
# 3.利用opener对象的open方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))






