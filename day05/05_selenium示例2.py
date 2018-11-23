from selenium import webdriver
# 操作键盘鼠标
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")
# 查找搜索框位置
driver.find_element_by_id("kw").send_keys(u"美女")
#driver.save_screenshot("美女.png")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.save_screenshot("搜索.png")














