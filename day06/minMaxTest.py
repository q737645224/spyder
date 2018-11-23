# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:24:28 2018

@author: Python
"""

#def maxMin(L): 
#   """
#   用递归算法求解一个数组的最大最小值
#   """
#   if len(L)<=2:
#       if len(L)==1:
#           return (L(0),L(0))
#       else:
#           if L(0)>L(1):
#               return (L(0),L(1))
#           return (L(1),L(0))
#   else:
#       if maxMin(L(:len(L)//2))>maxMin(L(len(L)//2:):
#           return(maxMin(L(:(len(L)//2)),maxMin(L(len(L)//2:))
#       return(maxMin(L(len(L)//2:),maxMin(L(:(len(L)//2)))

def myMaxMin(L, start, end):
    """
    递归来得到数组最大最小值
    """
    if end - start <= 1:#基准点的情况
        return ( max(L[start],L[end]),
                min(L[start],L[end]) )
    else:
        max1,min1 = myMaxMin(L, start, (start+end)//2)# 求左半部分
        max2,min2 = myMaxMin(L, (start+end)//2+1, end)# 求左半部分
        return max(max1,max2), min(min1,min2)
    
def maxMin(L): 
   """
   用递归算法求解一个数组的最大最小值
   """
   assert(type(L) == type([]) and len(L) > 0)
   maxV,minV = myMaxMin(L,0,len(L)-1)
   #print(maxV,minV)
   return maxV,minV

L = [5, 8, 4, 3, 1, -9]
assert(maxMin(L) == (8,-9))
#maxMin(5)













