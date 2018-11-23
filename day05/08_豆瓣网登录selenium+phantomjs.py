from selenium import webdriver
# 操作鼠标键盘
from selenium.webdriver.common.keys import Keys
# 创建phantomjs浏览器对象
driver = webdriver.PhantomJS()
driver.get("https://www.douban.com/")
driver.save_screenshot("豆瓣首页.png")

# 用户名
driver.find_element_by_name("form_email")\
                    .send_keys("309435365@qq.com")
# 密码
driver.find_element_by_name("form_password")\
                   .send_keys("zhanshen001")
# 验证码
key = input("请输入验证码:")
driver.find_element_by_id("captcha_field")\
                   .send_keys(key)
# 登录豆瓣
driver.find_element_by_class_name("bn-submit")\
                   .click()
driver.save_screenshot("登录成功.png")
driver.quit()



















