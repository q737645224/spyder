from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

result = driver.find_element_by_id("setf").text
print(result)
