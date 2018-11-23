# 导入selenium库中的webdriver
from selenium import webdriver
# 创建打开phantomjs的对象
driver = webdriver.PhantomJS()
# 访问百度
driver.get("http://www.baidu.com/")
# 获取网页截图
driver.save_screenshot("百度.png")


