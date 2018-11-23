import requests
import re
from pymysql import connect
import warnings

class MaoYanSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla4.0/"}
        self.page = 1
        self.offset = 0
        self.baseurl = "http://maoyan.com/board/4?offset="
        self.db = connect("localhost","root","123456",charset="utf8")
        self.cursor = self.db.cursor()
        
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
    def writeToMysql(self,content_list):
        c_db = "create database if not exists MaoYan;"
        u_db = "use MaoYan;"
        c_tab = "create table if not exists film(\
                 id int primary key auto_increment,\
                 name varchar(30),\
                 star varchar(50),\
                 time year)charset=utf8;"
        warnings.filterwarnings("error")
        try:
            self.cursor.execute(c_db)
        except Warning:
            pass

        self.cursor.execute(u_db)

        try:
            self.cursor.execute(c_tab)
        except Warning:
            pass

        for r_t in content_list:
            s_insert = "insert into film(name,star,time) \
                        values('%s','%s','%s')" % \
                        (r_t[0].strip(),r_t[1].strip(),
                         r_t[2].strip()[5:9])
            print(s_insert)
            self.cursor.execute(s_insert)
            self.db.commit()

    # 主函数
    def workOn(self):
        while True:
            url = self.baseurl + str(self.offset)
            print("正在爬取第%d页" % self.page)
            html = self.getPage(url)
            content_list = self.parsePage(html)
            self.writeToMysql(content_list)
            print("第%d页爬取成功" % self.page)
            
            c = input("是否继续爬取(y/n):")
            if c.strip().lower() == "y":
                self.offset += 10
                self.page += 1
            else:
                self.cursor.close()
                self.db.close()
                print("爬取结束,谢谢使用!")
                break

if __name__ == "__main__":
    spider = MaoYanSpider()
    spider.workOn()









