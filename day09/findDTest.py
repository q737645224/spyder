# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:18:50 2018

@author: Python
"""
def findDiff(L1, L2):
    sum1 = sum(L1)
    sum2 = sum(L2)
    if sum1 > sum2:
        return sum1-sum2
    else:
        return sum2-sum1

L1=[1,4,3,2,5]
L2=[1,4,3,5]
print(findDiff(L1,L2))
