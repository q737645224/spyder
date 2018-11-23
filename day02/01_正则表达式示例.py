import re

s = """<div><p>仰天大笑出门去,我辈岂是蓬蒿人</p></div>
<div><p>天生我材必有用,千金散尽还复来</p></div>"""
# 非贪婪匹配
p = re.compile('<div>.*?</div>',re.S)
result = p.findall(s)
print(result) # 列表中2个元素

# 创建编译对象,贪婪匹配
p = re.compile('<div>.*</div>',re.S)
result = p.findall(s)
print(result) # 列表中1个元素








#







