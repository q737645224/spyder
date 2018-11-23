import requests
import re
import pymongo

class MaoYanSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla4.0/"}
        self.page = 1
        self.offset = 0
        self.baseurl = "http://maoyan.com/board/4?offset="
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.MaoYan
        self.myset = self.db.film 
        
        
    # 获取html源码
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        return html

    # 正则解析html源码
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</div>',re.S)
        content_list = p.findall(html)
        # [("霸王别姬","张国荣","1993"),(),()]
        return content_list
    
    # 写入本地文件
    def writeToMongo(self,content_list):
        for r_t in content_list:
            d = {
                "name":r_t[0].strip(),
                "star":r_t[1].strip(),
                "time":r_t[2].strip()[5:9]
                }
            self.myset.insert(d)

    # 主函数
    def workOn(self):
        while True:
            url = self.baseurl + str(self.offset)
            print("正在爬取第%d页" % self.page)
            html = self.getPage(url)
            content_list = self.parsePage(html)
            self.writeToMongo(content_list)
            print("第%d页爬取成功" % self.page)
            
            c = input("是否继续爬取(y/n):")
            if c.strip().lower() == "y":
                self.offset += 10
                self.page += 1
            else:
                print("爬取结束,谢谢使用!")
                break

if __name__ == "__main__":
    spider = MaoYanSpider()
    spider.workOn()









