import requests
import re

class NeihanSpider:
    def __init__(self):
        self.baseurl = "http://www.neihanpa.com/article/index"
        self.page = 1
        self.headers = {"User-Agent":"Mozilla4.0/"}
    
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
        
    def parsePage(self,html):
        p = re.compile('<div class="desc">(.*?)</div>',re.S)
        r_list = p.findall(html)
        self.writePage(r_list)
    
    def writePage(self,r_list):
        for r_str in r_list:
            with open("内涵段子.txt","a") as f:
                r_str = r_str.strip().replace("\u3000","")
                f.write(r_str + "\n\n")
    
    def workOn(self):
        while True:
            if self.page == 1:
                url = self.baseurl + ".html"
            else:
                url = self.baseurl + "_" + str(self.page) + ".html"
            print("正在爬取第%d页" % self.page)
            self.getPage(url)
            print("第%d页爬取成功" % self.page)
            
            c = input("是否继续爬取(y/n):")
            if c == "y":
                self.page += 1
            else:
                print("爬取结束,谢谢使用!")
                break
                          
if __name__ == "__main__":
    spider = NeihanSpider()
    spider.workOn()














