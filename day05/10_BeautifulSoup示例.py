from bs4 import BeautifulSoup

html = "<div>九宵龙吟惊天变,风云际会浅水游</div>"
# 创建解析对象
soup = BeautifulSoup(html,'lxml')
# 查找div标签的文本
result = soup.div.string
print(result)