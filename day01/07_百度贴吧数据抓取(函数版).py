import urllib.request
import urllib.parse

# 得到html : 发请求获响应
def getPage(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req,timeout=10)
    html = res.read().decode("utf-8")
    return html

# 保存html到本地
def writePage(filename,html):
    with open(filename,"a",encoding="utf-8") as f:
        f.write(html)

# 主函数
def workOn():
    name = input("请输入贴吧名:")
    begin = int(input("请输入起始页:"))
    end = int(input("请输入终止页:"))
    baseurl = "http://tieba.baidu.com/f?"
    kw = {"kw":name}
    kw = urllib.parse.urlencode(kw)
    for page in range(begin,end+1):
        pn = (page-1) * 50
        url = baseurl + kw + "&pn=" + str(pn)
        print(url)
        print("正在下载第%d页" % page)
        html = getPage(url)
        filename = "第" + str(page) + "页.html"
        writePage(filename,html)
        print("第%d页下载成功" % page)
        
if __name__ == "__main__":
    workOn()





