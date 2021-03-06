"""
-------------------------------------------------------
作者 ：王汉志
github : https://github.com/HarchiCaibao
email : 1501859625@qq.com
date : 2018/12/12
使用pyecharts绘制各种图表
-------------------------------------------------------
"""
# coding=utf-8
import os
import jieba
import pickle
from pyecharts import Line
from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Radar
from wordcloud import WordCloud
# 折线图(2维)
def drawLine(title, data, savepath='./results'):
    line = Line(title)
    attrs = [data[i][0] for i in range(len(data))]
    values = [data[i][1] for i in range(len(data))]
    line.add('', attrs, values, is_smooth=True, mark_point=["max", "min"])
    line.render(os.path.join(savepath, '%s.html' % title))


# 饼图
def drawPie(title, data, savepath='./results'):
    pie = Pie(title)
    attrs = [data[i][0] for i in range(len(data))]
    values = [data[i][1] for i in range(len(data))]
    pie.add('', attrs, values, is_label_show=True)
    pie.render(os.path.join(savepath, '%s.html' % title))


# 柱状图
def drawBar(title, data, savepath='./results'):
    bar = Bar(title)
    attrs = [data[i][0] for i in range(len(data))]
    values = [data[i][1] for i in range(len(data))]
    bar.add('', attrs, values, mark_point=["min", "max"])
    bar.render(os.path.join(savepath, '%s.html' % title))


# 雷达图
def drawRadar(title, data, savepath='./results'):
    radar = Radar(title)
    values = [[data[i][1] for i in range(len(data))]]
    schema = [(data[i][0], 500) for i in range(len(data))]
    radar.config(schema)
    radar.add('', values, is_splitline=True, is_axisline_show=True)
    radar.render(os.path.join(savepath, '%s.html' % title))


# 词云
def drawWordCloud(words, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    wc = WordCloud(font_path='./fonts/simkai.ttf', background_color='black', max_words=2000, width=1920, height=1080,
                   margin=5)
    wc.generate_from_frequencies(words)
    wc.to_file(os.path.join(savepath, 'commentscloud.jpg'))


def calWordCount(texts, cutWord):
    """
    统计词频
    :param texts:待统计文本
    :param cutWord: 需忽略的词
    :return: dict：词频字典：key：词 value：频数
    """
    wordcount_dict = {}
    for text in texts:
        tt = jieba.cut(text)
        for t in tt:
            if t in cutWord:
                continue
            if t in wordcount_dict.keys():
                wordcount_dict[t] += 1
            else:
                wordcount_dict[t] = 1
    return wordcount_dict


if __name__ == '__main__':
    """
    f = open('./results/duye.pkl', 'rb')
    data = pickle.load(f)
    f.close()
    texts = [d[1][2] for d in data.items()]
    stopwords = open('./stopwords.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
    words_dict = statistics(texts, stopwords)
    DrawWordCloud(words_dict, savepath='./results')
    words_sorted = sorted(words_dict.items(), key=lambda item: item[1])
    data = words_sorted[-20:]
    DrawBar(title='高频词汇统计', data=data)
    stars = [d[1][1] for d in data.items()]
    star_dict = {}
    for star in stars:
        if star is None:
            continue
        if star in star_dict:
            star_dict[star] += 1
        else:
            star_dict[star] = 1
    data = list(star_dict.items())
    DrawPie(title='评分分布统计饼图', data=data, savepath='./results')
    DrawRadar(title='评分分布统计雷达图', data=data, savepath='./results')
    dates = [d[1][0] for d in data.items()]
    date_dict = {}
    for date in dates:
        if date in date_dict:
            date_dict[date] += 1
        else:
            date_dict[date] = 1
    data = sorted(list(date_dict.items()))
    drawLine(title='日期与评论数量', data=data, savepath='./results')
    """