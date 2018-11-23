from lxml import etree

html = """<div class="wrapper">
	<i class="iconfont icon-back" id="back"></i>
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
	</ul>
	<i class="iconfont icon-liebiao" id="menu"></i>
</div>"""
# 1.构建解析对象
parseHtml = etree.HTML(html)
# 2.解析对象调用 xpath 工具
# 获取所有a标签的 href属性值
r_list = parseHtml.xpath('//a/@href')
#for i in r_list:
#    print(i)
    
# 获取 / 
r_list = parseHtml.xpath(
                   '//a[@id="channel"]/@href')
#print(r_list)
# 获取 非 /
#r_list = parseHtml.xpath(
#                '//ul[@id="nav"]/li/a/@href')

r_list = parseHtml.xpath(
                '//ul[@id="nav"]//a/@href')
#print(r_list)
# 获取所有<a>节点的文本内容
r_list = parseHtml.xpath('//a')
# 得到的是元素对象,需要用 对象名.text 获取内容
#for i in r_list:
#    print(i.text)
# 获取 新浪社会
r_list = parseHtml.xpath('//a[@id="channel"]')
#for i in r_list:
#    print(i.text)
# 获取非 新浪社会 的节点文本
r_list = parseHtml.xpath('//ul[@id="nav"]//a')
for i in r_list:
    print(i.text)
















