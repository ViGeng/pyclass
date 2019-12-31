#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
'''
要求计算并打印有关文本文件内容的统计数据。包括：

1. 用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。

2. 文件中各字母（不区分大小写）出现的频率（所占百分比）。

3. 文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
'''

import string
import re


def statistic(text='bill.txt'):
    with open(text) as f:
        text = f.read()
        character_all = len(text)   #统计所有字符（包括空格与换行符）
        row_all = text.count('\n') + (text[-1] != '\n')  #计算所有行数（包括空白行）
    lines = text.splitlines()
    letter_count = {}
    letter_sum = 0
    word_count = {}
    word_sum = 0
    remain = ''  #保留上一行-前的内容

    for i in string.ascii_lowercase:
        letter_count[i] = 0
    for line in lines:
        if line.strip():
            for key in letter_count:       
                letter_count[key] += line.lower().count(key)
                letter_sum += line.lower().count(key)
            #计算每一行字母（小写）形式的个数，并累计总的字母的个数
            line = line.strip().lower()
            if remain:
                line = remain + line
                remain = ''
            if line[-1] == '-' and line[-2] in string.ascii_lowercase:   #查看上一行是否以ab-结尾
                line = line[:-2]
                while line and line[-1] in string.ascii_lowercase:      #在该行不空并且最后的字母部分还没转移完时把字母部分转移到remain中 
                    remain = line[-1] + remain
                    length = len(line)
                    line = line[:length-1]
                
            
            words = re.findall(r'\b[a-z]+\'*\-*[a-z]+\b',line)
            #统计一行内所有的单词
            #单词规则为字母开头中途可以有'、-类的连接符，例如ab'(cd)、ab-cd
            #文本中有出现‘abc--df’的语句，按理说应该有空格隔开为‘abc -- bf’，并且数目不多，这里不再细分；个别个例也不做细分.
            word_sum += len(words)
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    
    def letter_frequency():
        letter_percentage = {}
        for key in letter_count:
            letter_percentage[key] = '%2.2f' % (100*letter_count[key]/letter_sum) + '%'
        return letter_percentage


    def frequent_words():
        n = 10
        exclusion_dict = {'the','and','i','to','of','a','you','my','that','in','on', \
                          'for','not','with','me','it','she','he','be','is','be','your',\
                          'this','his','but','as','have','so','him','will','at','they',\
                          'what','by','are','her','do','we','shall','or','our','all','if','from'}
        #一个排除虚词等频繁出现的词的字典(通常英文中的代词也去掉） 但是没有去掉古英语中的一些代词
        top_ten = [(0,0)] * 10
        #创建一个序列先放入十个元素,目的是为了从大到小记录前十个出现频率最高的单词
        min_number = 0  #记录当前被选单词最小的出现频数
        min_count = 10  #记录最小频数的单词的个数

        for word in word_count:
            if word in exclusion_dict or word in string.ascii_lowercase:
                continue
            else:
                number = word_count[word]
                if number > min_number:
                    i = 0
                    while number < top_ten[i][1]:
                        i += 1
                    top_ten = top_ten[0:i] + [(word,number)] + top_ten[i:]
                    if len(top_ten) - min_count >= n:    #当最小频数的单词们可以被删去时删除 并重新计算最小频数以及最小频数的单词的个数
                        top_ten = top_ten[0:n]
                        min_number = top_ten[-1][1]
                        j = 0
                        while min_number < top_ten[j][1]:
                            j += 1
                        min_count = n - j
                elif number == min_number:
                    top_ten += [(word,number)]
                    min_count += 1
        return top_ten
            
    return (character_all, row_all, word_sum),letter_frequency(),frequent_words()




if __name__ == '__main__':
    basic_information,letter_percentage,top_ten = statistic()
    print('以下为文本内容的统计数据:')
    print('本文一共有%d个字符，%d行，%d个单词' % basic_information)
    print('-'*40)
    print('单词出现频率如下：')
    for i in string.ascii_lowercase:
        print(i,letter_percentage[i],sep='\t')
    print('-'*40)
    print('最高频数的十个单词及其出现次数如下(从大到小)：')
    for word in top_ten:
        print(word[0],word[1],sep='\t')

    
    
    
