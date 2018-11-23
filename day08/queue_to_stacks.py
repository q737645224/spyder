# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:48:21 2018

@author: Python
"""

def in_queue(L1,L2):
#    while True:
#        m = input("输入数据，空行结束:")
#        if not m:
#            break
#        else:
#            L1.append(m)
    L1 = [1,2,3,4,5]
    L1 = stacks_to_queue(L1,L2)
    return L1

def stacks_to_queue(L1,L2):
    for i in range(len(L1)-1):
        L2.append(L1.pop(0))
    for i in range(len(L2)-1):
        for i in range(len(L2)-1):
            L2.append(L2.pop(0))
        L1.append(L2.pop(0))
    L1.append(L2.pop(0))
    return L1

def out_queue(L1):
    return L1.pop(0)

L1 = []
L2 = []
L1 = in_queue(L1,L2)
for i in range(len(L1)):
    print(out_queue(L1))