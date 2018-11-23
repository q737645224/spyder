from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.PhantomJS()
driver.get("https://www.douyu.com/directory/all")

while True:
    # 创建解析对象
    soup = bs(driver.page_source,"lxml")
    # 直接调用方法去查找元素
    # 存放所有主播的元素对象
    names = soup.find_all('span',{"class":"dy-name ellipsis fl"})
    numbers = soup.find_all('span',{"class":"dy-num fr"})
    # name,number是一个对象,get_text()
    for name,number in zip(names,numbers):
        print("\t观众人数:",number.get_text().strip(),
              "\t主播名字:",name.get_text().strip())
    
    if driver.page_source.find("shark-pager-disable-next") == -1:
       driver.find_element_by_class_name("shark-pager-next").click()
       time.sleep(4)
    else:
        break
    
    









