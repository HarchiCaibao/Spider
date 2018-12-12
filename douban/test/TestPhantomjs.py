# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
#火狐浏览器驱动
#driver_path = "D:\Python\geckodriver-v0.15.0-win64\geckodriver.exe"
#谷歌浏览器驱动
driver_path = "D:\Python\chromedriver_win32\chromedriver.exe"

login_url = "https://www.douban.com/accounts/login?source=movie"

"""
使用seleium登录豆瓣
username：用户名
password：登录密码
对于验证码，无法自动识别，会下载到本地，手动输入即可
"""
def loginDouban(username,password):
    #打开谷歌浏览器
    bro = webdriver.Chrome(executable_path=driver_path)
    bro.get(login_url)
    email_i = bro.find_element_by_id("email")
    password_i = bro.find_element_by_id("password")
    email_i.send_keys(username)
    password_i.send_keys(password)
    #判断是否需要输入验证码

def openBaiduAndSearch(key):
    bro  = webdriver.Chrome(executable_path=driver_path)
    bro.get("https://www.baidu.com/")
    kw = bro.find_element_by_id("kw")
    kw.send_keys("python")
    kw.send_keys(Keys.ENTER)
    """
    wait = WebDriverWait(bro, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    """
    print(bro.current_url)
    time.sleep(3)
    bro.close()
if __name__ == "__main__":
    username = "13148933354"
    password = "wws1121150*"
    #loginDouban(username,password)
    openBaiduAndSearch("python")