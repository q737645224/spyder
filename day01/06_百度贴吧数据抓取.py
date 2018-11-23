import urllib.request
import urllib.parse

baseurl = "http://tieba.baidu.com/f?"
headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}

name = input("请输入贴吧名:")
begin = int(input("请输入起始页:"))
end = int(input("请输入终止页:"))
# URL进行编码
kw = {"kw":name}
kw = urllib.parse.urlencode(kw)
# 写循环拼接URL,发请求获响应,写入本地文件
for page in range(begin,end+1):
    # 拼接URL
    pn = (page-1)*50
    url = baseurl + kw + "&pn=" + str(pn)
    # 发请求,获响应
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8") # 字符串
    # 写文件/保存到本地
    filename = "第" + str(page) + "页.html"
    with open(filename,"w",encoding="utf-8") as f:
        print("正在下载第%d页" % page)
        f.write(html)
        print("第%d页下载成功" % page)
        print("*" * 30)

















