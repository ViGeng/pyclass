#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# File     : Big_Project.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/12/04

'''

    要求计算并打印有关文本文件内容的统计数据。包括：

    1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。

    2。文件中各字母（不区分大小写）出现的频率（所占百分比）。

    3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数

 

    测试数据是莎士比亚全集，“bill.txt”文件，文件大小5.6M字节。

'''
def detect_encoding(text):
    """探测文件的编码方式
    参数：文件名， 返回探测到的编码方式
    """

    # UTF-8-SIG
    encodings = 'ASCII', 'UTF-8', 'GBK'

    for encoding in encodings:
        try:
            with open(text, encoding=encoding) as file:
                file.read(100)
            break
        except UnicodeDecodeError:
            pass
    return encoding



def char_count(text,encoding):
    '''计算并指定文本文件中包含多少字符（包括空白字符）
    参数：文件名，文件编码方式，返回统计的字符数
    '''
    with open(text,'r',encoding=encoding) as file:
        lines = file.readlines()

    count = 0

    for line in lines:
        count += len(line)

    return count


def line_count(text,encoding):
    '''计算指定文本文件中包含多少行
    参数：文件名，文件编码方式，返回统计的行数
    '''
    with open(text,'r',encoding=encoding) as file:
        count = -1
        
        for count,line in enumerate(file):
            pass
        count +=1
    #lines = len(file.readlines())
        
    return count


def word_count(text,encoding):
    '''计算指定文本文件中包含多少单词
    参数：文件名，文件编码方式，返回统计的单词数
    '''    
    import string
    with open(text,'r',encoding=encoding) as file:
        lines = file.readlines()
    count = 0
    for line in lines:
        
        words = 0
        inword = False
        for c in line:
            
            if inword:
                if c not in string.ascii_letters and c != '-':
                    inword = False
                elif c == '-':
                    inword = True
                    words -= 1
            else:
                if c in string.ascii_letters:
                    inword = True
                    words += 1
        count = count + words
    
    return count

def letter_count(text,encoding):
    '''计算并打印指定文本文件中各字母（不区分大小写）出现的频率（所占百分比）
    参数：文件名，文件编码方式，返回值为空
    '''
    
    letterCounts = {}
    letterSum = 0
    for i in range(97, 123):
        letterCounts[chr(i)] = 0

    with open(text,'r',encoding=encoding) as file:
        lines = file.readlines()
        for line in lines:
            for letter in line:
                if ord(letter) in range (97,123):
                    letterCounts[letter] += 1
                    letterSum += 1
                elif ord(letter) in range (65,91):
                    letterCounts[chr(ord(letter)+32)] += 1
                    letterSum += 1

    for key,value in letterCounts.items():
        print('The frequency of letter {:} is {:}%.'.format(key,100*value/letterSum))    


def FrequentWord_Count(text,encoding):
    '''计算并打印指定文本文件中出现次数最多的十个单词
    参数：文件名，文件编码方式，返回值为空
    '''
    import re
    from matplotlib import pyplot as plt
    
    word_dic = {}

    with open(text,'r',encoding=encoding) as file:
        lines = file.readlines()

    for line in lines:
        line = re.sub('\W',' ',line)
        line_word=line.split()

        for word in line_word:
            lower_word = word.lower()
            if not word_dic.get(lower_word):
                word_dic[lower_word] = 1
            else:
                word_dic[lower_word] += 1

    word_sorted = sorted(word_dic.items(),key=lambda d:d[1],reverse = True )

    for i in range(10):
        print('Word \'%-6s\' shows %-6d times.' %(word_sorted[i][0],word_sorted[i][1]))

if __name__ == '__main__':

    text='bill.txt'
    encoding=detect_encoding('bill.txt')
    print('-'*60)
    print('This text file contains %d characters,%d lines and %d words.'%(char_count(text,encoding),line_count(text,encoding),word_count(text,encoding)))
    print('-'*60)
    letter_count(text,encoding)
    print('-'*60)
    FrequentWord_Count(text,encoding)
    print('-'*60)
