#coding=utf-8
import json
def test1():
    file  = open("单机热游.json","r",encoding="utf-8")
    data = json.load(file)
    #print(type(data))
    for con in data:
        print(con["conten_list_name"]+": "+con["conten_list_url"])

if __name__ =="__main__":
    test1()