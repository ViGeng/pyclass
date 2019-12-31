#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import re
#计算一个字符串中有多少个单词的函数
def wordnumber(sentence):
    pattern=re.compile(r'\b\w+\b')
    word=pattern.findall(sentence)
    n=len(word)
    return(n)

if __name__=='__main__':
    text=open('bill.txt','r')
    textlist=text.readlines()
    linesnumber=len(textlist)#行数

    characternumber=0
    wordsnumber=0
    for i in range(len(textlist)):
        characternumber=characternumber+len(textlist[i])#字符数累加
        wordsnumber=wordsnumber+wordnumber(textlist[i])#单词数累加
    #打印字符数、行数、单词数
    print('文件包含%d个字符，%d行，%d个单词\n' % (characternumber,linesnumber,wordsnumber))


    count=[0]
    countlist=count*26
    alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #逐行统计字母的个数，并将每一个字母的对应数量按顺序放入长度为26的列表countlist里
    for l in range(len(textlist)):
        #将每一个字符串变成与大小写无关的形式
        casefoldlist=textlist[l].casefold()
        for a in range(26):
            countlist[a]+=casefoldlist.count(alphalist[a])

    #逐个计算26个字母的出现频率并打印
    for b in range(26):
        print('字母%s或%s出现的频率为%.2f%%' % (alphalist[b],alphalist[b].upper(),(countlist[b]/sum(countlist))*100))
        

    text=open('bill.txt','r')
    article=text.read()
    allword=re.findall(r'\b\w+\b',article)
    pattern=re.compile(r'\b\w+\b')
    allword=pattern.findall(article)
    dicwords=dict()
    ignorelist=['the','d','and','to','of','that','a','is','s','with','And','in','not','be','for']#排除词列表
    for w in allword:
        if w not in ignorelist:
            dicwords[w]=dicwords.setdefault(w,0)+1
    sortresult=sorted(dicwords.items(),key=lambda d:d[1],reverse=True)[:10]

    print('\n出现频率最高的10个单词为：')
    for i in range(len(sortresult)):
        print('%s出现的次数为%d' % (sortresult[i][0],sortresult[i][1]))


    

    
           
            









    
    


