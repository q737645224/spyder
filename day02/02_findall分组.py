import re

s = "A B C D"
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

# 1.按整体去匹配 ['A B','C D']
# 2.显示括号()中内容 ['A','C']
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))

# 1.整体匹配 ：['A B','C D']
# 2.显示括号内容 ：[('A','B'),('C','D')]
p3 = re.compile('(\w+)\s(\w+)')
print(p3.findall(s))




















