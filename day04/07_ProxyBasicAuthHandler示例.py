import urllib.request

server = "114.67.228.126:16819"
user = "309435365"
password = "szayclhp"
url = "http://www.baidu.com/"
tarenaUrl = "http://code.tarena.com.cn/"

# 密码管理器对象操作
pwd = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd.add_password(None,server,user,password)
#pwd.add_password(None,tarenaUrl,"tarenacode","code_2013")
# 创建处理器对象
proxy_handler = urllib.request.ProxyBasicAuthHandler(pwd)
opener = urllib.request.build_opener(proxy_handler)
# 发请求
req = urllib.request.Request(url)
res = opener.open(req)
html = res.read().decode("utf-8")
print(html)



















