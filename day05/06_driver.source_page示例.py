from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

r1 = driver.page_source.find("kw") # 能找到 17556
r2 = driver.page_source.find("aaaaaaa") # 失败-1
print(r1,r2)
