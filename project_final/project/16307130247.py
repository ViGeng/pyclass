#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from collections import Counter
import re
def remove_punctuation(text):
    #移除标点符号
    remove_chars = '[!"#$%&()*+,./:;<=>?@？“”‘’！[\\]^`{|}~]+'
    return re.sub(remove_chars, '', text)

def count_alphabet_freq(text_file_path,alphabet_freq):
    #统计字母频率
    f = open(text_file_path, 'r', encoding='utf8')
    text = f.read().lower()
    number_of_alphabet = len(text)
    alphabet_count = Counter(list(text))
    for chr in alphabet_freq:
        if( chr in alphabet_count):
            alphabet_freq[chr] = alphabet_count[chr]
    alphabet_freq_item = alphabet_freq.items()
    sum = 0
    for t in alphabet_freq_item:
        sum+= t[1]
    for t in alphabet_freq:
        alphabet_freq[t] = alphabet_freq[t]/sum
    f.close()
    return number_of_alphabet,alphabet_freq

def count_line_word(text_file_path):
    #统计行数、词数、词频
    f = open(text_file_path, 'r', encoding='utf8')
    textlines = f.readlines()
    n_line = len(textlines)
    all_word = []#存放所有词
    connection = ''
    for line in textlines:
        line = remove_punctuation(line)
        line_list = line.split()
        if(line_list!=[]):
            if line_list[-1][-1] =='-':#检查行尾最后一个词是否有连字符
                connection = line_list[-1][:-1]
                del line_list[-1]
                all_word +=line_list
            else:
                if connection=='':
                    all_word +=line_list
                else:
                    line_list[0] = connection+line_list[0]
                    connection = ''
                    all_word +=line_list
    word_freq = Counter(all_word)

    n_word = len(all_word)
    f.close()
    return n_line, n_word, word_freq
def remove_word_from_freq(word_freq,word_remove_list):
    #将不要的词去掉
    for word in word_remove_list:
        del word_freq[word]
    return word_freq
def top_10_word(word_freq):
    #返回词频前十的词
    n = min(len(word_freq),10)
    top_ten_tuple = sorted(word_freq.items(),key = lambda element:element[1],reverse = True)[:n]
    return top_ten_tuple
def output(n_alphabet,n_line,n_word,alphabet_freq,top_ten_tuple):
    print('该文本文件的统计如下')
    print('-'*20)
    print('含有%d个字符\n含有%d行\n含有%d个单词'%(n_alphabet,n_line,n_word))
    print('-'*20)
    print('字母频率如下\n')
    print('{:>2s}\t{:<10s}'.format('字母', '频率'))
    for alphabet in alphabet_freq:
        print('{:>2s}\t{:<10s}'.format(alphabet, str(alphabet_freq[alphabet]*100)[:4]+' %'))
    print('-'*20)
    print('出现频率最多的10个词如下\n')
    print('{:>10s}\t{:<10s}'.format('词', '频数'))
    for word in top_ten_tuple:
        print('{:>10s}\t{:<10s}'.format(word[0], str(word[1])))
def main():
    text_file_path = 'bill.txt'
    word_remove_list = ['the','you']#你不想要的词

    alphabet_freq = {chr(i):0 for i in range(97,123)}
    n_alphabet,alphabet_freq = count_alphabet_freq(text_file_path,alphabet_freq)#统计有多少字符，并统计了字母频率
    n_line, n_word, word_freq = count_line_word(text_file_path)#统计行数，统计了词频，和总词数
    
    word_freq = remove_word_from_freq(word_freq,word_remove_list)
    top_ten_tuple = top_10_word(word_freq)
    output(n_alphabet,n_line,n_word,alphabet_freq,top_ten_tuple)

if __name__ == '__main__':
    main()
    

