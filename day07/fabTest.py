# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:12:47 2018

@author: Python
"""

#def Fab(n):
#    """
#    用循环前n个斐波那契数列的值
#    """
#    prev=1
#    current=1
#    print(current)
#    for i in range(1,n):
#        print(current)
##        next=prev+current
##        prev = current
##        current=next
#        prev,current=current,prev+current
#
#Fab(10)

def Fab(n):
    index,a,b=0,0,1
    while index < n:
        a,b = b,a+b
        index += 1
        yield a
    #return a

#for i in range(1,11):
#    print(Fab(i))        

for i in Fab(10):
    print(i)

# n = 10, index = 0,  a = 0, b = 1
#      a = 1, b = 1, index = 1 
#       此时此刻 Fab会保存当前a,b,index状态,
#       记录下一条语句的位置
# 下一次执行时: a = 1, b = 2, index = 2
#       此时此刻 Fab会保存当前a,b,index状态,
#       记录下一条语句的位置
# 下一次执行时: a = 2, b = 3, index = 3
#       此时此刻 Fab会保存当前a,b,index状态,
#       记录下一条语句的位置 
# ...
#       
# 下一次执行时: a = X, b = Y, index = 10
 


















    