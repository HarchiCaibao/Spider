import json
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"}
def getHtml(url):
    re = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(re)
    html = res.read()
    return html
"""
保存分类信息，包括名字和详细分类的url
html:各分类html文件
"""
def saveContent(html):
    html = BeautifulSoup(html,'lxml')

    content = html.select('a[class="clickstat"]')
    #print content
    #print "***********************************************"
    for site in content[2:content.__len__()]:
        con_url =  site.attrs['href']
        con = site.select('span')[0].get_text()
        saveContenList(con_url,con)
"""
保存每个大分类中的小分类信息，包括名字和跳转的url
url:分类跳转url
conName：分类名称
"""
def saveContenList(url,conName):
    re = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(re)
    html = BeautifulSoup(res.read(),'lxml')
    output = open(conName+".json","wb")
    contens = html.select('li[class="game-list-item"]')
    conten_lists = []
    for site in contens:
        conten_list = {}
        list_url = site.select('a')[0].attrs['href']
        list_name = site.select('a h3')[0].text
        conten_list["conten_list_name"] = list_name
        conten_list["conten_list_url"] = list_url
        conten_lists.append(conten_list)
    line = json.dumps(conten_lists,ensure_ascii=False)
    #保存到文件
    output.write(line.encode("utf-8"))
    output.close()
if __name__=="__main__":
    url = "https://www.huya.com/g"
    print("开始爬取")
    html = getHtml(url)
    print("开始保存")
    saveContent(html)
    print("虎牙直播分类收视数据爬取成功！")