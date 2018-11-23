import requests
from lxml import etree

class BaiduImageSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla5.0/"}
        self.baseurl = "http://tieba.baidu.com"
        self.pageurl = "http://tieba.baidu.com/f?"
    # 获取每个帖子的url
    def getPageUrl(self,params):
        # 得到贴吧第1页html源码
        res = requests.get(self.pageurl,params=params,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # 从html源码获取帖子链接 '/p/2323432'
        parseHtml = etree.HTML(html)
        t_list = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
#        ['/p/2342443','/p/08098034']
        for t in t_list:
            t_url = self.baseurl + t
            self.getImageUrl(t_url)
        
    # 获取帖子中所有图片的URL
    def getImageUrl(self,t_url):
        # 获取帖子的html源码,为了从中筛选图片URL
        res = requests.get(t_url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # 得到图片URL
        parseHtml = etree.HTML(html)
        i_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        #['http://...jpg','http://...png',...]
        for i in i_list:
            self.writeImage(i)
        
    # 保存到本地
    def writeImage(self,i):
        # 获取图片的html源码 bytes
        res = requests.get(i,headers=self.headers)
        res.encoding = "utf-8"
        html = res.content
        # 保存到本地
        filename = i[-10:]
        with open(filename,"wb") as f:
            print("%s正在下载" % filename)
            f.write(html)
            print("%s下载成功" % filename)
            
    # 主函数
    def workOn(self):
        name = input("请输入贴吧名字:")
        begin = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))
        for page in range(begin,end+1):
            pn = (page-1)*50
            params = {
                    "kw":name,
                    "pn":str(pn)
                 }
            self.getPageUrl(params)
    
if __name__ == "__main__":
    spider = BaiduImageSpider()
    spider.workOn()

        
    
    
    
    
    
    
    
    
    
    
    
    








