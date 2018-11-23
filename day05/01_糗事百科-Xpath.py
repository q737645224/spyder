import requests
from lxml import etree
import pymongo

class QiuShiSpider:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/8hr/page/8/"
        self.headers = {"User-Agent":"Mozilla5.0"}
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.BaiKe
        self.myset = self.db.baiketab
        
    def getPage(self):
        res = requests.get(self.url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        # 基准xpath,每个段子节点对象的列表
        base_list = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        # 遍历每个段子的节点对象
        for children in base_list:
            # 用户昵称
            username = children.xpath('./div/a/h2')[0].text
            # 段子内容
            content = children.xpath('.//div[@class="content"]/span')[0].text
            # 好笑数量
            laughNum = children.xpath('.//i')[0].text
            # 评论数量
            pingNum = children.xpath('.//i')[1].text
    
            d = {"username": username.strip(),
                 "content" : content.strip(),
                 "laughNum": laughNum.strip(),
                 "pingNum" : pingNum.strip()
              }
            self.myset.insert(d)
    
if __name__ == "__main__":
    spider = QiuShiSpider()
    spider.getPage()
    
    
    
    
    
    
    
    
    
    
    
    
    








