import urllib.request
import re

class MaoYanSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla4.0/"}
        self.page = 1
        self.offset = 0
        self.baseurl = "http://maoyan.com/board/4?offset="
        
    # 获取html源码
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    # 正则解析html源码
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</div>',re.S)
        content_list = p.findall(html)
        # [("霸王别姬","张国荣","1993"),(),()]
        return content_list
    
    # 写入本地文件
    def writePage(self,content_list):
        for m_tuple in content_list:
            for n_str in m_tuple:
                with open("猫眼电影.txt","a",encoding="utf-8") as f:
                    f.write(n_str.strip() + "\n")
            
            with open("猫眼电影.txt","a",encoding="utf-8") as f:
                f.write("\n\n")
    # 主函数
    def workOn(self):
        while True:
            url = self.baseurl + str(self.offset)
            print("正在爬取第%d页" % self.page)
            html = self.getPage(url)
            content_list = self.parsePage(html)
            self.writePage(content_list)
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









