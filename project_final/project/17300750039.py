#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
'''
要求计算并打印有关文本文件内容的统计数据。包括：

1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。

2。文件中各字母（不区分大小写）出现的频率（所占百分比）。

3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
'''
    
def Statistics(text):
    text_letters = list(text)
    count = 0
    for i in text_letters:
        if i.isalpha():
            count += 1
    
    text_lines = text.splitlines()
    newlines = [i for i in text_lines if i !='']

    import re
    words = re.sub('-\n*','',text.lower()) #将折行单词重新组成单词
    text_words = re.findall(r'\b\w+\b',words)

    
    print('字符数（含数字、标点及空字符等）：%d'%len(text_letters))
    print('字符数（只含字母）：%d'%count)
##    print(text_letters[:100])
    print('行数（含空行）：%d'%len(text_lines))
    print('行数（不含空行）：%d'%len(newlines))
##    print(text_lines[:10])
    print('单词数：%d'%len(text_words))
##    print(text_words[:100])
    return text_letters,text_lines,text_words
    
def letter_frequency(letter): #方法一：使用count函数统计字母
    count1 = []
    sum1 = 0
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter=[item.lower() for item in letter]
    for i in letters:
        count1.append(letter.count(i))
        sum1 += letter.count(i)
##    print(count1)
    print('各个字母出现的频率：')
    for j in range(26):
        print('%s\t%f%%'%(letters[j],count1[j]/sum1*100))
    pass

def letter_frequency1(letter): #方法二：使用字典统计字母
    count3 = {}
    import re
    for i in letter:
        if i.isalpha():
            if i.lower() in count3:
                count3[i.lower()] += 1
            else:
                count3[i.lower()] = 1
    sum3 = sum(count3.values())
    print('各个字母出现的频率：')
    for j in sorted(count3):
        print('%s\t%f%%'%(j,count3[j]/sum3*100))

def word_frequency(word):
    count2 = {}
    for i in word:
        if i.lower() in count2:
            count2[i.lower()] += 1
        else:
            count2[i.lower()] = 1
    word_count = sorted(count2.items(),key=lambda item: item[1],reverse=True)
    print('出现频率最高的10个单词及出现的次数（已排除部分单词）：')
    j = 0
    n = 0
    word_except=['the','and','i','to','of','a','my','in','is','not'] #排除单词列表
    while True:
        if word_count[j][0] in word_except:
            j += 1
        else:
            print('%s\t%d'%(word_count[j][0],word_count[j][1]))
            n += 1
            j += 1
        if n == 10:
            break
    pass

if __name__ == '__main__':
    with open('bill.txt','r') as file:
        text = file.read()
    letter,line,word = Statistics(text)
    print()
##    letter_frequency(letter)
    letter_frequency1(letter)
    print()
    word_frequency(word)
    
