#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

def statistics_1(filename):
    '''统计文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词'''
    with open(filename,'r') as f:
        lines = f.readlines()
        line_num = len(lines)
        char_num = 0
        i = 0
        for line in lines:
            char_num += len(line)
            if '-\n' in line:
                i += 1
        file = ' '.join(lines)
        word_num = len(file.split()) - i

    print('该文本共有{0}个字符,{1}行，{2}个单词'.format(char_num,line_num,word_num))
            

def statistics_2(filename):
    '''统计文本文件中各字母（不区分大小写）出现的频率（所占百分比）'''
    with open(filename,'r') as f:
        f_list = f.read()
        f_string = ''.join(f_list)
        f_string = f_string.lower()
        d = {}
        import string
        for i in string.ascii_lowercase:
            d[i] = 0
        for i in f_string:
            if i in string.ascii_lowercase:
                d[i] += 1
        Sum = sum(d.values())
    for i in d.keys():
        print('字母{0}出现的频率为{1:5.2f}%'.format(i,d[i]/Sum*100))
            
    
def statistics_3(filename):
    '''统计文件中出现频率最高的10个单词及它们出现的次数，忽略集合{"the","and","i","to","of","a","you","my","that","in","is","not","for",\
            "with","me","it","be","your","this","his","but","he","as","have","thou",\
            "so","him","will","what","by","thy","all","are","her","no","do","shall",\
            "if","we","or","thee","our","on","from","at","they","which","would","more",\
            "was","o","then","she","am","how","their","them","than","may","'tis","these",\
            "th'","any","who","too","can","exit","men","why","i'll","an"}的元素'''
    with open(filename,'r') as f:
        lines = f.readlines()
        text = []
        for line in lines:
            if '-/n' in line:
               line = line.rstrip('-/n')
            text.append(line)
        lines_str = ''.join(text)
        lines_str = lines_str.lower()
        import re
        pattern = '[a-z\-\']+'
        words_list = re.findall(pattern,lines_str)
        excludes = {"the","and","i","to","of","a","you","my","that","in","is","not","for",\
                    "with","me","it","be","your","this","his","but","he","as","have","thou",\
                    "so","him","will","what","by","thy","all","are","her","no","do","shall",\
                    "if","we","or","thee","our","on","from","at","they","which","would","more",\
                    "was","o","then","she","am","how","their","them","than","may","these",\
                    "th'","any","who","too","can","exit","men","why","i'll","an"}
        d = {}
        for word in words_list:
            if word not in excludes:
                d[word] = d.get(word,0) + 1
        items = sorted(list(d.items()),key = lambda item:item[1],reverse = True)
        print('文件中出现频率最高的10个单词及它们出现的次数为')
        for i in range(10):
            print('%s \t %d'%(items[i][0],items[i][1]))


def main():
    filename = 'bill.txt'
    print('-'*40)
    print()
    statistics_1(filename)
    print()
    print('-'*40)
    print()
    statistics_2(filename)
    print()
    print('-'*40)
    print()
    statistics_3(filename)
    print()
    print('-'*40)

if __name__  =='__main__':
    main()
    
