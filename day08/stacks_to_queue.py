# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:38:03 2018

@author: Python
"""
## stack queue heap
#def in_stacks(L1,L2):
##    while True:
##        m = input("输入数据，空行结束:")
##        if not m:
##            break
##        else:
##            L1.append(m)
#    L1 = [1,2,3,4,5]
#    for i in range(len(L1)):
#        L2.append(L1.pop())
#    return L2
#
#def out_stacks(L2):
#    return L2.pop()
#
#L1=[]
#L2=[]
#L2 = in_stacks(L1,L2)
#print(L2)
#for i in range(len(L2)):
#    print(out_stacks(L2))

class QueueWithStacks:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, e):
        self.s1.append(e)
    
    def pop(self):
        if (len(self.s2) == 0):
            while(len(self.s1) > 0):
                t = self.s1.pop()
                self.s2.append(t)
        assert(len(self.s2) > 0)# 此时说明队列没有元素
        return self.s2.pop()
    
q = QueueWithStacks()
q.push('a')
q.push('b')
q.push('c')
print(q.pop())
print(q.pop())
print(q.pop())

















    
    
    