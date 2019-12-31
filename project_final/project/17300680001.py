#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import string
import re

def openfile(text = 'bill.txt'): #打开文件，返回一个列表（元素为每一行的字符串）和文本（文本对连字符进行了处理）
    with open(text) as f:
        alist = f.readlines()
        text_str = ''.join(alist)
        pattern = r'(\w*)-\n\n'
        text_str = re.sub(pattern,r'\1',text_str)
    return alist,text_str

def character_count(alist): #用作统计字符的函数
    character = 0
    for line in alist:
        character = character + len(line)
    return character

def letter_frequency(alist): #对列表中所有字母（将所有字母转化为小写）计数，并汇总在一个字典里，返回字典，字典格式为{'a':其个数,'b':其个数...}
    letter_count = {}

    for line in alist:
        lower_line = line.lower()
        for i in lower_line:
            if i in string.ascii_lowercase:
                letter_count[i] = letter_count.get(i,0) + 1

    for m in string.ascii_lowercase:
        if m not in letter_count:
                letter_count[m] = 0
    return letter_count

def words_frequency(all_words): #用字典统计每一个单词出现的次数
    words_dict = {}
    for word in all_words:
        words_dict[word] = words_dict.get(word,0) + 1
    return words_dict



if __name__ == '__main__':
    alist , text_str = openfile('bill.txt') #读取文件，返回列表和字符串
    
    #1、统计用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词
    character = character_count(alist) #统计字符
    words = len(text_str.split()) #统计单词数，单词是通过文本中空格进行分割计数
    how_many_lines = len(alist) #统计行数
    print('文本文件中包含',character,'个字符',sep = '')
    print('文本文件中包含',how_many_lines,'行',sep = '')
    print('文本文件中包含',words,'个单词',sep = '')
    print()

    #2、统计文件中各字母（不区分大小写）出现的频率（所占百分比）
    letter_count = letter_frequency(alist)
    for n in string.ascii_lowercase:
        total_letter = sum(letter_count.values()) #求出所有字母总和
        print('%s%s%s%s%6.2f%s'%(n.upper(),'或',n,'的出现频率为:',letter_count[n]/total_letter*100,'%'))
    print()

    #3、统计文件中出现频率最高的10个单词及它们出现的次数
    all_words = [each_word.strip(string.punctuation).lower() for each_word in text_str.split()] #删去所有标点符号，并将大写转为小写
    words_dict = words_frequency(all_words)
    not_count = input('请输入排除词，不区分大小写，并用空格隔开:').lower() #创建要排除的词的列表
    for key in words_dict.copy(): #将排除词移除字典
        if key in not_count.split():
            del words_dict[key]

    sorted_w_d = sorted(words_dict.items(),key = lambda item:item[1],reverse = True) #按照每个单词出现的次数排序字典
    print()
    print('忽略排除词后出现频率最高的10个单词是:')
    print()
    print('%s %-15s%10s'%('序号','单词','出现次数'))
    for times in range(10):
        print('%2d   %-15s    %10d'%(times + 1,sorted_w_d[times][0],sorted_w_d[times][1])) #打印字典排序后的列表前10项
