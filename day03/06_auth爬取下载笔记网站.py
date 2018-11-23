import requests
import re

class NoteSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla5.0/"}
        # auth为元组
        self.auth = ("tarenacode","code_2013")
        self.url = "http://code.tarena.com.cn/"
    
    def getParsePage(self):
        res = requests.get(self.url,auth=self.auth,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        p = re.compile('<a href="\w+/">(.*?)</a>',re.S)
        r_list = p.findall(html)
        # 调用writePage方法写入本地文件
        self.writePage(r_list)
    
    def writePage(self,r_list):
        print("开始写入")
        for r_str in r_list:
            with open("达内笔记.txt","a") as f:
                f.write(r_str + "\n")
        print("写入完成")

if __name__ == "__main__":
    spider = NoteSpider()
    spider.getParsePage()
    
    
    
    
    
    
    
    
    







