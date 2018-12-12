import json
from urllib import request
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"}

def getContent(fileName):
    contenFile = open(fileName,"r",encoding="utf-8")
    contenLists = json.load(contenFile)
    juedi = contenLists[0]
    juedi_url = juedi["conten_list_url"]
    html = openUrl(juedi_url)
    getWatchNums(html)
    """
    for con in contenLists:
        con_name = con["conten_list_name"]
        con_url = con["conten_list_url"]
        html = openUrl(con_url)
    """
def openUrl(url):
    req = request.Request(url,headers=headers)
    return request.urlopen(req).read()
def getWatchNums(html):
    bs_html = BeautifulSoup(html,"lxml")
    #<i class="js-num">81.4万</i>
    #<i class="nick" title="bb文">bb文</i>
    txt = bs_html.select('span[class="txt"]')
    print(txt.__len__())
    for data in txt:
        nick = data.select('i[class="nick"]')[0].text
        js_num = data.select('i[class="js-num"]')[0].text
        print(nick+":"+js_num)
if __name__ == "__main__":
    getContent("单机热游.json")