# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:01:48 2018

@author: Python
"""

#create database if not exists MaoYan charset utf8;
#use MaoYan;
#create table Film(id int, title varchar(30), star varchar(100),
#releasetime varchar(80));
#SELECT count(*) FROM `MaoYan`.`Film`;


import random
import re
import json
from multiprocessing import Pool
#from multiprocessing import Lock
from multiprocessing import Manager
import functools
import basicSpider
import myPymysql

count = 0
def write2Sql(item):
    global count
    count += 1
    print(count)
    sqlHelper = myPymysql.DBHelper()
    title = item['title']
    print(title)
    star = item['actor']
    print(star)
    time = item['releasetime']
    print(time)
    sql = "INSERT INTO MaoYan.Film(id,title,star,releasetime)VALUES(%s,%s,%s,%s);" 
    params = (str(count), title, star, time)
    sqlHelper.execute(sql,params)
    sqlHelper.close()

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
        #write2File(item)
        write2Sql(item)
        lock.release()

import matplotlib.pyplot as plt#用这个库来画图
def AnalysisCountry():
  dbhelper = myPymysql.DBHelper()
  # 统计数据
  total = dbhelper.fetchCount("SELECT count(*) FROM `MaoYan`.`Film`;")
  Am=dbhelper.fetchCount("SELECT count(*) FROM `MaoYan`.`Film` WHERE releasetime like '%美国%';")
  Ch=dbhelper.fetchCount("SELECT count(*) FROM `MaoYan`.`Film` WHERE releasetime like '%中国%';")
  Jp=dbhelper.fetchCount("SELECT count(*) FROM `MaoYan`.`Film` WHERE releasetime like '%日本%';")
  Ko=dbhelper.fetchCount("SELECT count(*) FROM `MaoYan`.`Film` WHERE releasetime like '%韩国%';")
  others=total-Am-Ch-Jp-Ko

  #
  x = Am,Ch,Jp,Ko,others
  labels='America','China','Japan','Korea','Others'
  colors='Blue','Red','Yellow','Green','White'
  plt.pie(x,labels=labels,colors=colors)
  plt.show()
  dbhelper.close()


if __name__ == "__main__":
  AnalysisCountry()
   # L = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
   #       "Opera/8.0 (Windows NT 5.1; U; en)",
   #       "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
   #       "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"
   #       ]
   
   # manager = Manager() # 当你需要使用进程池来操作Lock时,需要这个大神
   # lock = manager.Lock()
   
   # #需要另一个大神functools来将原函数包装一下,进行传lock
   # partial_CrawlMovieInfo = functools.partial(CrawlMovieInfo, lock)
   # pool = Pool()
   # pool.map(partial_CrawlMovieInfo, [i*10 for i in range(10)])
   # pool.close()
   # pool.join()
     
   # print("over")
   
   
   
   
    
    #headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36")]
    #print(basicSpider.downloadHtml('http://maoyan.com/board/4?offset=0', headers=headers))