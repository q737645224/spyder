# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:08:11 2018

@author: Python
"""
from urllib import request
from urllib import error
from urllib import parse
import random
import time


def downloadHtml(url, headers=[()], proxy={},
                 timeout=None, decodeInfo="utf-8",
                 num_tries=10, useProxyRatio=11):
    """
    写一个完善一点下载网页的逻辑
    支持UA等Http Request Headers
    支持Proxy
    超时的考虑
    编码的问题,如果不是UTF-8编码怎么办
    服务器错误返回5XX怎么办
    客户端错误返回4XX怎么办
    考虑延时的问题
    """
    #time.sleep(random.randint(1,2))#控制访问,不要太过频繁
    
    # 通过useProxyRatio来调整是否使用代理
    if random.randint(1,10) > useProxyRatio:
        proxy = None
    
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxy_support)
    # 设置user-agent
    opener.addheaders = headers
    # 安装opener
    request.install_opener(opener)
    
    html = None
    try:
        # 这里可能出现很多异常
        # 可能会出现编码异常,
        # 可能会出现网络下载异常:客户端的异常 404, 403
        #                      服务器的异常 5XX
        res = request.urlopen(url)
        html = res.read().decode(decodeInfo)
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
    except error.URLError or error.HTTPError as e:
        # 客户端的异常 404, 403
        if hasattr(e, 'code') and 400 <= e.code < 500:
            print("Client Error"+e.code)
        elif hasattr(e, 'code') and 500 <= e.code < 600:
            if num_tries > 0:
                time.sleep(random.randint(1,3))# 这里等待的时间可以不断的增加
                downloadHtml(url, 
                             headers, 
                             proxy,
                             timeout,
                             decodeInfo,
                             num_tries-1)
                
    return html
        

if __name__ == "__main__":
    headers = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36")]
    print(downloadHtml('http://maoyan.com/board/4?offset=0', headers=headers))
        
        
        
        
        
        
        
    
    