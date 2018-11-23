import requests
import re
import pymongo

class LianJiaSpider:
    def __init__(self):
        self.baseurl = "https://bj.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent":"Mozilla5.0/"}
        self.proxies = {"HTTP":"http://309435365:szayclhp@114.67.228.126:16819"}
        self.page = 1
        # 创建连接对象
        self.conn = pymongo.MongoClient("localhost",27017)
        # 创建数据库对象
        self.db = self.conn.Lianjia#库名
        #　创建集合对象
        self.myset = self.db.housePrice#表名

    # 获取页面
    def getPage(self,url):
        res = requests.get(url,proxies=self.proxies,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    # 用正则解析页面
    def parsePage(self,html):
        p = re.compile('<div class="houseInfo">.*?data-el="region">(.*?)</a>.*?<div class="totalPrice">.*?<span>(.*?)</span>',re.S)
        r_list = p.findall(html)
        # [("首科花园","595"),(),()]
        self.writeToMogo(r_list)
        
    # 保存本地文件
    def writeToMogo(self,r_list):
        for r_tuple in r_list:
            d = {"houseName":r_tuple[0].strip(),
                 "housePrice":float(r_tuple[1].strip())*10000}
            self.myset.insert(d)
        print("存入mongodb数据库成功")
        # mongo
        # show dbs;
        # use Lianjia;
        # show tables;
        # db.housePrice.find().pretty();



    # 主函数
    def workOn(self):
        while True:
            print("正在爬取%d页" % self.page)
            # 拼接URL
            url = self.baseurl + str(self.page) + "/"
            self.getPage(url)
            print("第%d页爬取成功" % self.page)
            
            c = input("是否继续爬取(y/n):")
            if c.strip().lower() == "y":
                self.page += 1
            else:
                print("爬取结束,谢谢使用!")
                break
            
if __name__ == "__main__":
    spider = LianJiaSpider()
    spider.workOn()





    
    
    
    
    
    
    
    
    
    

