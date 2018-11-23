import urllib.request
import urllib.parse

class BaiduSpider:
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com/f?"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    
    # 请求并读取页面内容
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    # 保存到本地文件
    def writePage(self,filename,html):
        with open(filename,"a",encoding="utf-8") as f:
            f.write(html)
    
    # 主函数
    def workOn(self):
        name = input("请输入贴吧名:")
        begin = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))
        kw = {"kw":name}
        kw = urllib.parse.urlencode(kw)
        for page in range(begin,end+1):
            pn = (page-1) * 50
            url = self.baseurl + kw + "&pn=" + str(pn)
            print("正在下载第%d页" % page)
            html = self.getPage(url)
            filename = "第" + str(page) + "页.html"
            self.writePage(filename,html)
            print("第%d页下载成功" % page)        
    
if __name__ == "__main__":
    # 创建对象
    spider = BaiduSpider()
    # 对象调用类内方法
    spider.workOn()
    
    
    
    
    
    
    
    
    
    
    
    








