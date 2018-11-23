# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:42:16 2018

@author: Python
"""

from bs4 import BeautifulSoup
import re

import basicSpider


def get_html(url):
    """
    获取一页的网页源码信息
    """
    headers = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")]
    html = basicSpider.downloadHtml(url, headers=headers)
    return html

def get_movie_all(html):
    """
    获取当前页面中所有的电影的列表信息
    """
    soup = BeautifulSoup(html, "html.parser")
    movie_list = soup.find_all('div', class_='bd doulist-subject')
    #print(movie_list)
    return movie_list

def get_movie_one(movie):
    """
    获取一部电影的精细信息，最终拼成一个大的字符串
    """
    result = ""
    soup = BeautifulSoup(str(movie),"html.parser")
    title = soup.find_all('div', class_="title")
    soup_title = BeautifulSoup(str(title[0]), "html.parser")
    for line in soup_title.stripped_strings:
        result += line
    
    try:
        score = soup.find_all('span', class_='rating_nums')
        score_ = BeautifulSoup(str(score[0]), "html.parser")
        for line in score_.stripped_strings:
            result += "|| 评分："
            result += line
    except:
         result += "|| 评分：5.0"
         
    abstract = soup.find_all('div', class_='abstract')
    abstract_info = BeautifulSoup(str(abstract[0]), "html.parser")
    for line in abstract_info.stripped_strings:
        result += "|| "
        result += line    
    
    result += '\n'
    #print(result)
    return result

def save_file(movieInfo):
    """
    写文件的操作,这里使用的追加的方式来写文件
    """
    with open("doubanMovie.txt","ab") as f:
        f.write(movieInfo.encode("utf-8"))
    
crawl_queue = []    # 待爬队列
crawled_queue = []  # 已爬队列
    
def CrawlMovieInfo(url):
    """
    抓取一页数据的逻辑
    """
    global crawl_queue
    global crawled_queue
    
    try:
        # 处理当前页的待爬URL
        print(url)
        html = get_html(url)
        pattern = re.compile('(https://www\.douban\.com/doulist/3516235/\?start=.*)"')
        itemUrls = re.findall(pattern, html)
        # print(itemUrls)
        # print(len(itemUrls))
        
        # 两步去重
        for item in itemUrls:
            # 这里需要将item转换成HASH
            if item not in crawled_queue:#已爬队列的去重
                crawl_queue.append(item)
        crawl_queue = list(set(crawl_queue))#待爬队列的去重
        
        # 处理当前页的数据
        moviesList = get_movie_all(html)
        for it in moviesList:
            save_file(get_movie_one(it))
        
        crawled_queue.append(url)# 这里需要将URL转换成HASH
            
    except:
        pass


if __name__ == "__main__":
    
    # https://www.douban.com/doulist/3516235/?start=0&sort=seq&playable=0&sub_type=
    #CrawlMovieInfo("https://www.douban.com/doulist/3516235/?start=0&sort=seq&playable=0&sub_type=")
    
    # 广度优先遍历
    seed_url = "https://www.douban.com/doulist/3516235/?start=0&sort=seq&playable=0&sub_type="
    crawl_queue.append(seed_url)
    
    while crawl_queue:
        url = crawl_queue.pop(0)
        CrawlMovieInfo(url)
        
    print(crawled_queue)
    
    














