# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:01:48 2018

@author: Python
"""

import basicSpider
import random
import re
import json
from multiprocessing import Pool
#from multiprocessing import Lock
from multiprocessing import Manager




def write2File(item):
    with open("猫眼电影2.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')

def parseOnePage(html):
    pattern = re.compile('<div class="movie-item-info">[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    results = re.findall(pattern, html)
    for it in results:
        yield{"title":it[0].strip(),
              "actor":it[1].strip(),
              "releasetime":it[2].strip()}

def CrawlMovieInfo(lock, offset, ua="Opera/8.0 (Windows NT 5.1; U; en)"):
    """
    抓取猫眼电影数据
    """
    # 抓取页面
    url = "http://maoyan.com/board/4?offset="+str(offset)
    headers = [("User-Agent",ua)]
    html = basicSpider.downloadHtml(url, headers=headers)
    # 提取内容,存储
    for item in parseOnePage(html):
        lock.acquire()
        write2File(item)
        lock.release()


if __name__ == "__main__":
   L = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
         "Opera/8.0 (Windows NT 5.1; U; en)",
         "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
         "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"
         ]
   
   #url = "http://maoyan.com/board/4?offset="
#   for i in range(10):
#       CrawlMovieInfo(url+str(i*10), ua=random.choice(L))
       
   manager = Manager()
   lock = manager.Lock()
   
   #需要另一个大神functools来将原函数包装一下,进行传lock
   pool = Pool()
   pool.map(CrawlMovieInfo, [i*10 for i in range(10)])
   pool.close()
   pool.join()
     
   print("over")
   
   
   
   
    
    #headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36")]
    #print(basicSpider.downloadHtml('http://maoyan.com/board/4?offset=0', headers=headers))