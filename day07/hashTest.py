# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:04:08 2018

@author: Python
"""

import hashlib

def hashStr(strInfo):
    """
    对字符串进行hash
    """
    hashObj = hashlib.sha256()
    hashObj.update(strInfo.encode("utf-8"))
    return hashObj.hexdigest()


CHUNCKSIZE = 2048#不要出现magic number
def hashFile(fileName):
    """
    对文件进行hash
    """    
    hashObj = hashlib.sha256()
    with open(fileName, 'rb') as f:
        while True:
            # 这个地方不能一次性读取出来,
            #如果文件太大,内存不够
            chunk = f.read(CHUNCKSIZE)
            if not chunk:
                break
            hashObj.update(chunk)
    return hashObj.hexdigest()
    
print(hashStr("hello"))
print(hashFile("day07.txt"))    
    
    
    
    
    
    
    
    
    