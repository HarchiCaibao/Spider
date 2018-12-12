"""
-------------------------------------------------------
作者 ：王汉志
github : https://github.com/HarchiCaibao
email : 1501859625@qq.com
date : 2018/12/12
-------------------------------------------------------
"""
# coding=utf-8

import pickle
class testPyecharts:
    def __init__(self,fileName):
        print(fileName)
    def getDataFromPkl(self,fileName):
        f = open(fileName,"rb")
        datas_dict = pickle.load(f)
        for keys in datas_dict.items():
            print(keys)
        f.close()

if __name__ == "__main__":
    tp = testPyecharts("./results/duye.pkl")
    tp.getDataFromPkl("./results/duye.pkl")
