#作者 ：王汉志
#github : https://github.com/HarchiCaibao
#email : 1501859625@qq.com
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time
import os
import pickle
import json

# 火狐浏览器驱动
# driver_path = "D:\Python\geckodriver-v0.15.0-win64\geckodriver.exe"
# 谷歌浏览器驱动
driver_path = "D:\Python\chromedriver_win32\chromedriver.exe"

login_url = "https://www.douban.com/accounts/login?source=movie"

class douban:
    def __init__(self):
        self.bro = webdriver.Chrome(driver_path)
        self.data = {}
        self.comment_url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'

    def _login_douban(self,username,password):
        """
        使用seleium登录豆瓣
        验证码需手动输入
        :param username: 登录的用户名
        :param password: 登录密码
        :return: none
        """
        self.bro.get(login_url)
        email_input = self.bro.find_element_by_id("email")
        password_input = self.bro.find_element_by_id("password")
        email_input.send_keys(username)
        password_input.send_keys(password)
        #判断是否需要输入验证码
        if self.element_is_exit("captcha_field"):
           img_url = self.bro.find_element_by_id("captcha_image").get_attribute("src")
           print("验证码地址为:%s"%img_url)
           captch = input("请输入验证码：")
           self.bro.find_element_by_id("captcha_field").send_keys(captch)
        self.bro.find_element_by_name("login").send_keys(Keys.ENTER)
        time.sleep(3)

    def get(self, url, username=None, password=None):
        """
        评论爬取
        :param url: 需要爬取电影的评论url
        :param username: 登录的用户名
        :param password: 登录密码
        :return: 实际爬取的评论总数
        """
        if not (username is None or password is None):
            self._login_douban(username,password)
            print("登录成功!")
        sid = re.findall('subject/(\d*)/', url)[0]
        i = -1
        error_num = 0
        while True:
            i += 1
            print('正在爬取第%d页的评论' % i)
            comment_url = self.comment_url.format(sid, i * 20)
            #打开评论地址
            self.bro.get(comment_url)
            soup = BeautifulSoup(self.bro.page_source, 'lxml')
            infos = soup.find_all('div', attrs={'class': 'comment-item'})
            for info in infos:
                try:
                    nickname = info.find('a', attrs={'title': True}).get('title')
                except:
                    error_num += 1
                    continue
                try:
                    star, date = info.find_all('span', attrs={'title': True})
                    star = float(re.findall('allstar(\d\d).*?', str(star))[0]) / 10
                except:
                    star = None
                    date = info.find_all('span', attrs={'title': True})[0]
                date = date.string.strip()
                comment = info.find('span', attrs={'class': 'short'}).string.strip()
                self.data[nickname] = [date, star, comment]
            if error_num > 2:
                break
        print("正在保存数据.......")
        #self.save_as_pkl()
        self.save_as_json()
        return len(self.data.keys())

    def save_as_pkl(self,savepath="./results",savename=None):
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        if savename is None:
            savename = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))+".pkl"
        f = open(os.path.join(savepath, savename), 'wb')
        pickle.dump(self.data,f)
        f.close()
        print("数据保存成功")

    def save_as_json(self,savepath="./jsons",savename=None):
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        if savename is None:
            savename = time.strftime("%Y-%m-%d_%H-%M-%S")+".json"
        output = open(os.path.join(savepath,savename),"wb")
        line = json.dumps(self.data,ensure_ascii=False)
        output.write(line.encode("utf-8"))
        output.close()
        print("保存成功，格式为json")

    def closeBrowser(self):
        self.bro.close()

    def element_is_exit(self,id):
        """
        通过id判断元素是否存在
        :param id: 元素id
        :return: True：存在
        """
        try:
            self.bro.find_element_by_id(id)
            return True
        except:
            return False

"""
def test_save_as_pkl():
    db = douban()
    db.save_as_json()
"""

if __name__ == "__main__":
	username = "11111111" #your username for login
	password = "11111111" #your password for login
    db = douban()
    duye_url = "https://movie.douban.com/subject/3168101/comments?status=P"
    comment_sums = db.get(duye_url,username,password)
    db.closeBrowser()
    print("共爬取：%d条评论" % comment_sums)