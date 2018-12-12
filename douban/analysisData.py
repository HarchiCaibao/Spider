"""
-------------------------------------------------------
作者 ：王汉志
github : https://github.com/HarchiCaibao
email : 1501859625@qq.com
date : 2018/12/12
-------------------------------------------------------
"""
# coding=utf-8
import drawByEcharts as draw
import pickle
class analysis:
    def __init__(self,fileName):
        """
        加载评论数据
        :param fileName: 评论数据保存的路径
        """
        self.fileName = fileName
        f = open(self.fileName,"rb")
        self.data_dict = pickle.load(f)
        f.close()
    def draw_comment_date_line(self):
        """
        绘制评论与日期分布折线图
        :return: None
        """
        date_dict = {}
        dates = [d[1][0] for d in self.data_dict.items()]
        for date in dates:
            if date in date_dict:
                date_dict[date] +=1
            else:
                date_dict[date] = 1
        #按时间排序
        datas = sorted(list(date_dict.items()))
        draw.drawLine("日期与评论折线图",datas)

    def draw_wordCount_bar(self):
        texts = [d[1][2] for d in self.data_dict.items()]
        f = open("./stopwords.txt","r",encoding="utf-8")
        #[:-1]除去最后一个元素
        cutWords = f.read().split('\n')[:-1]
        f.close()
        wordCount_dict = draw.calWordCount(texts,cutWords)
        #key=lambda x: x[1] ：表示按照字典的值来排序
        words_sorted = sorted(wordCount_dict.items(), key=lambda x: x[1])
        #取最大的三十个数
        datas = words_sorted[-30:]
        draw.drawBar("高频词汇柱状图",datas)

if __name__ == "__main__":
    an = analysis("./results/duye.pkl")
    an.draw_comment_date_line()
    an.draw_wordCount_bar()
