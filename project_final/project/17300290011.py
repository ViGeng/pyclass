#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
'''
要求计算并打印有关文本文件内容的统计数据。包括：
1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。
2。文件中各字母（不区分大小写）出现的频率（所占百分比）。
3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的
所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
'''


import re 
import operator


# 包含多少字符

def count_each_char_sort_value(string):
    
    string = re.sub('\n','',string)
    char_number = len(string)
   
    print("\n共有字符(包含空格)  :%-10d" %char_number)


# 包含多少行(不统计空行)

def count_valid_lines(f):
    
    
    lines_number = 0
    
    for line in f:
        if not line.isspace():
            lines_number += 1
    
    print("\n共有行数(不包含空行):%-10d" %lines_number)



#统计单词的个数  和文件中出现频率最高的10个单词及它们出现的次数

#对文本进行处理，先转化成小写，之后删除特殊字符，并且讲每行最后带有-连词符号的单词化为普通单词。

def get_word_count_text(text):    
           
    for ch in "~@#$%^&*()!_-+=<>?/,.:;{}[]|\'""":    
        text=text.replace(ch,' ')
    #剔除末尾连字符       
    text = re.sub('-\n','',text)
    
    text =  text.lower()  
    
    return text    



def count_word_sort_by_value(string):
    
    #排除词库
    excludes = ['the','and','to','of','i','a','in','it','that','is',
            'you','my','with','not','his','this','but','for',
            'me','s','he','be','as','so','him','your','d']

    
    word_text = get_word_count_text(string)
    #对空格切片
    words = word_text.split()

    counts={}    
    sumcount = 0  
    for word in words:    
        counts[word]=counts.get(word,0)+1  
        sumcount = sumcount + 1 
    
    #复制字典，排除词库
    counts_ex = counts.copy()    
    for key in counts.keys():
        if key in excludes:
            counts_ex.pop(key)
    items=list(counts_ex.items())    
    items.sort(key=lambda x:x[1],reverse=True)    
    
    print('\n单词总个数:',sumcount)
    print('除词库外，出现次数最多的10个单词：')
    for i in range(10):    
        word,count=items[i]    
        print('{0:<12}{1:>5}'.format(word,count))  

#文件中各字母（不区分大小写）出现的频率（所占百分比）。
def count_letter_number_and_frequency(string):
    text = string.lower()
    letter = dict()
    sumcount = 0
    for i in text:
        if i.isalpha():
            letter[i] = letter.get(i,0)+1
            sumcount += 1
    #计算频率
    for key in letter.keys():
        letter[key] = letter[key]/sumcount*100 
    
    letter = sorted(letter.items(),key = operator.itemgetter(1),reverse = True)

    print("\n字母出现的频率：")
    for i in letter:
        print("{0:}: {1:>2.2f} %".format(*i))
    


def main():
    fr = open('bill.txt','rt',encoding='utf-8')
    text = fr.read()
    fr.seek(0)
    
    count_valid_lines(fr)
    count_each_char_sort_value(text)
    count_word_sort_by_value(text)
    count_letter_number_and_frequency(text)

    fr.close()

if __name__ == '__main__':
    main()

