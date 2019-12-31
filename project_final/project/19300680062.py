#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#大作业 作者：19级经济学院 应眺
def statistics():
    file = input('请输入你想打开的文件名')
    with open(file,'r') as f:
        text = f.read()
    text = text.lower()
    print('该文本包含%i个字符'%len(text),end = ', ')
    print('共有%i行'%len(text.splitlines()),end = ', ')
    words = tuple(text.split())
    print('%i个单词'%(len(words)-text.count('-\n')))
    
    print('各字母出现的频率如下：')
    amount = {}
    for i in range(97,123):
        amount[chr(i)] = text.count(chr(i))
    percentage = {}
    for letter in amount:
        percentage[letter] = amount[letter]/sum(amount.values())*100
        print(f'{letter}:{percentage[letter]:5.2f}%',end = '\t')
    print()
    vocabulary = {}
    for word in words:
        if word not in vocabulary:
            vocabulary[word] = 1
        else:
            vocabulary[word] = vocabulary[word] + 1
    ##注：曾用代码
    ##      for word in words:
    ##          if word not in vocabulary:
    ##              vocabulary = words.count(word)
    ##      但是电脑计算非常缓慢（两分钟没有得到结果），不知是何原因

    print('出现次数最多的10个单词：')
    words_sorted = sorted(vocabulary, key = lambda key: vocabulary[key])
    values_sorted = sorted(vocabulary.values())
    top10 = list(zip(words_sorted[:-11:-1],values_sorted[:-11:-1]))
    for i in range(10):
        print('第%2i名：%-6s%5i次'%(i+1 ,*top10[i]))
    exclusion = ['the','i','and','to','of','a','my','in','you','is',\
                 'that','not','with']
    
    print('除去部分常见词后出现次数最多的单词')
    for word in exclusion:
        del vocabulary[word]
    words_sorted1 = sorted(vocabulary, key = lambda key: vocabulary[key])
    values_sorted1 = sorted(vocabulary.values())
    newtop10 = list(zip(words_sorted1[:-11:-1],values_sorted1[:-11:-1]))
    for i in range(10):
        print('第%2i名：%-6s%5i次'%(i+1 ,*newtop10[i]))

if __name__ == '__main__':
    statistics()
