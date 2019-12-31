# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#大作业

import os

def get_article_information():  # 字符数
    curretn_path = os.getcwd()
    file_name = os.path.join(curretn_path,u'bill.txt')
    with open(file_name,'r') as f:
        lines = f.readlines()
    return lines

def statistics_character_count(lines=None):
    character_number = 0
    for line in lines:
        character_number += len(line)
    return character_number

def statistics_line_number(lines=None): # 行数
    line_number = len(lines)
    return line_number

def statistics_word_number(lines=None):  #单词个数
    word_number = 0
    for line in lines:
        line = line.replace('\n','')
        line_split = line.split()
        if len(line_split) == 0:
            continue
        else:
            if line_split[-1].endswith('-'):
                word_number += (len(line_split) - 1)
            else:
                word_number += len(line_split)
    return word_number

def statistics_alph_rate(lines=None):  #字母出现的频率
    res = dict()
    for line in lines:
        line = str(line.replace('\n',''))
        for string in line:
            if string.isalpha():
                i = string.lower()
                if i not in res:
                    res[i] = 1
                else:
                    res[i] += 1
    res_rate = dict()
    alp_count = 0
    for key in list(res.keys()):
        alp_count += res[key]
    print('*' * 40)
    for key in list(res.keys()):
        res_rate[key] = res[key] / alp_count * 100
        print(u'字母 %s 百分比为: %s' %(key,res_rate[key]))
    return res

def statistics_top(lines=None,topn=None):
    delete_word= ['the','I','and','to','of','is','you']
    word_dict = dict()
    for line in lines:
        line = line.replace('\n','')
        line_split = line.split()
        for word in line_split:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    for word in delete_word:
        del word_dict[word]
    static_word = {v:i for i,v in word_dict.items()}
    word_keys = list(static_word.keys())
    word_keys.sort(reverse=True)
    word_topn = word_keys[:topn]
    word_res_dict = dict()
    for word in word_topn:
        word_res_dict[static_word[word]] = word
    return word_res_dict


def main():

    inforamtion = get_article_information()
    character_number = statistics_character_count(lines=inforamtion)
    print(u'包含字符数为: %s'%character_number)
    line_number = statistics_line_number(lines=inforamtion)
    print(u'包含行数为: %s' %line_number)
    word_number = statistics_word_number(lines=inforamtion)
    print(u'包含单词个数为: %s' %word_number)
    res = statistics_alph_rate(lines=inforamtion)
    word_topn = statistics_top(lines=inforamtion,topn=10)
    print('*' * 40)
    print(u'出现频率最高的10个单词以及次数为:')
    for key in word_topn:
        print(u'%s频率为: %s' %(key,word_topn[key]))


if __name__ == '__main__':
    main()
