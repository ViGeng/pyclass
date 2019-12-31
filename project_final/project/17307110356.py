#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

'''
    要求计算并打印有关文本文件内容的统计数据。包括:

    1. 用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、
多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。

    2. 文件中各字母（不区分大小写）出现的频率（所占百分比）。

    3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是
一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的所有单词，
然后统计这张表以外出现频率最高的10个单词以及其出现的次数.

    测试数据是莎士比亚全集，“bill.txt”文件，文件大小5.6M字节。

'''

'''
    1. 读取文件
    2. 统计字符数；行数、单词数 --> 分割存储列表，len()
    3. 统计26个字母数（不分大小写），分别计算频率（百分比）
    4. （基于2.3）统计同一单词出现的次数，取top10；
        *创建排除词列表后，在新列表中找到top10

'''

import string

'''基础统计'''

def character_num(text):           #字符数统计
    print('字符数：%s' % (str(len(text))))

    pass


def line_num(text):              #统计行数
    f_line = text.splitlines()
    print('行数：%s' % (str(len(f_line))))

    pass


def word_num(text):
    '''统计单词数'''
    f_all = text.replace('-\n\n','').replace('*',' ')                          #去除*
    words_num = 0

    f_words = f_all.split()                                   #粗暴分隔

    null = 0                                          #去除纯标点符号
    for i in f_words:
        if i.strip("'") == '':
            null += 1

    words_num = len(f_words) - null #- additional

    print('单词个数（包含连字符连接词和缩写词）：%s' % str(words_num))

    pass


def letters_frequency(text):
    '''字母（不区分大小写）出现频率统计'''

    d_num = dict.fromkeys(string.ascii_lowercase, 0)
    f_all = text.lower().replace('-\n\n','').replace('*','')                  #全部转化为小写，去除连字符+*

    for s in f_all:
        if s in string.ascii_lowercase:
            d_num[s] += 1

    print('各字母出现的频率为（不区分大小写）：')
    for key in d_num:
        print('{} :'.format(key), '{0:>5.2f}%'.format(d_num[key] / len(f_all) * 100))

    pass


def find_top_words(text):
    '''高频单词top10'''

    f_all = text.lower().replace('-\n\n','').replace('*',' ')                #全部小写    #replace替换后字符串本身不变？！
    f_split_1 = f_all.split()

    word_freq = {}                         #词频统计存储对象
    for i in f_split_1:
        if i not in word_freq:
            word_freq[i] = 1
        else:
            word_freq[i] += 1

    word_sort = sorted(word_freq.items(), key = lambda item:item[1], reverse = True)       #按value排序
    word_sorted = {k:v for k,v in word_sort}

    def pick_top_words(word_sorted):
        '''在排好的字典里选出前10个'''
        top_words = {}
        for i,(k,v) in enumerate(word_sorted.items()):
            if i <= 10:
                top_words[k] = v
        print('出现频率最高的10个单词及其次数分别为：')
        for key in top_words:
            print('{:<6}：'.format(key), '{0:>5}'.format(top_words[key]))

    pick_top_words(word_sorted)                                                          #第一次选top10

    except_words = ['he', 'she', 'me','my', 'i', 'him', 'her', 'his', 'they',             #排除词列表
    'them', 'their','you', 'your', 'a', 'of', 'the', 'this', 'that', 'is', 'to',
    'not', 'it', 'and', 'as']

    print()
    print('-' * 50)
    print()
    print('排除词列表：{}'.format(except_words))
    print()

    word_sorted_2 = word_sorted
    try:
        for i in except_words:
            del word_sorted_2[i]
    except KeyError as note:
        note

    print('{:-^30}'.format('剔除排除词后'))
    pick_top_words(word_sorted_2)                                               #第二次选top10

    pass


if __name__ == '__main__':

    f = open('bill.txt', encoding = 'utf-8')
    text = f.read()

    character_num(text)
    line_num(text)
    word_num(text)

    print()
    print('-'*50)
    print()

    letters_frequency(text)

    print()
    print('-'*50)
    print()

    find_top_words(text)


    f.close()
