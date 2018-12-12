"""
-------------------------------------------------------
作者 ：王汉志
github : https://github.com/HarchiCaibao
email : 1501859625@qq.com
date : 2018/12/12
-------------------------------------------------------
"""
# coding=utf-8
import jieba

def test1():
    str1 = "渣渣辉是个辣中鸡鸡中翅"
    texts = jieba.cut(str1)
    for tt in texts:
        print(tt)
    #print(jieba.lcut((str1)))

if __name__ == "__main__":
    lists = [1,2,3,4,5,6,7,8,9,10]
    datas = lists[:3]
    print(datas)