# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:26:41 2018

@author: Python
"""

#有10个球,每个球有两种颜色的选择:黑与白;
#使用递归的方法把这10个球所有的颜色可能性打印出来;
#0000000000
#1000000000
#...
#1111111111
count = 0
def perm(n, begin, end):
    """
    递归归的方法把这10个球所有的颜色可能性打印出来
    """
    global count
#    n=0
#    perm(n, begin+1, end)
#    n=1
#    perm(n, begin+1, end)
    if begin == end:# 基准点
        print(n)
        count += 1
    else:
       perm(n, begin+1, end)
       n[begin] = (n[begin]+1)%2 # 1<->0
       perm(n, begin+1, end)
       
L = [0,0,0,0,0,0,0,0,0,0]
perm(L, 0, len(L))
print(count)

       
       
       
        
    
    
    
    
    