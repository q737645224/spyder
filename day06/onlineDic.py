# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:34:14 2018

@author: Python
"""

import urllib
import json

import time
import random
import hashlib

def getSalt():
    return str(int(time.time()*1000)+random.randint(0,11))

def getSign(key,salt):
    #print(key)
    #print(salt)
    sign = ("fanyideskweb" + key + salt + "6x(ZHw]mwzX#u0V7@yfwK")
    hashObj = hashlib.md5()
    hashObj.update(sign.encode("utf-8"))
    return hashObj.hexdigest()
# 设置一个退出程序的出口
isOut = False

# 不断调用爬取翻译页面的功能
#直到isOut被设置为True，退出程序
while True:
    if isOut == True:
        break
    
    #假定用户输入“CloseMe”，则退出
    key = input("请输入需要翻译的文字，\
                输入CloseMe表示退出:\n")
    if key == "CloseMe":
        isOut = True
        continue #回到循环开始处，然后结果条件满足退出
    
    # 做真正的查询操作
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
       
    # http://tool.chinaz.com/js.aspx
    # 把form数据转规范化，然后post给服务端
    saltInfo = getSalt()
    formdata = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":saltInfo,
    "sign":getSign(key,saltInfo),
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
    }

    data = urllib.parse.urlencode(formdata).encode()
    # 给服务器发送post请求
    
        # 构造headers
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
               "X-Requested-With": "XMLHttpRequest",
               "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Content-Length":len(data),
               "Cookie":"YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=1547024714@106.38.155.125; OUTFOX_SEARCH_USER_ID_NCOO=305129980.33",
               "Connection":"keep-alive",
               "Accept":"application/json, text/javascript, */*; q=0.01",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Host":"fanyi.youdao.com",
               "Referer":"http://fanyi.youdao.com/"
            }
    req = urllib.request.Request(url,
                                 data,
                                 headers,
                                 method="POST")

    response = urllib.request.urlopen(req)
    info = response.read().decode("utf-8")
    #print(info)


    # json decode: json str --> dict
    jsonLoads = json.loads(info)
    print(jsonLoads['translateResult'][0][0]["src"])
    print(jsonLoads['translateResult'][0][0]["tgt"])