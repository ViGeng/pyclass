#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import re

#第一题：求文件行数、单词数和总字符数
with open ('bill.txt') as file:
    file1 = file.read()
    characters = len(file1)           
    lines = len(file1.split('\n'))
    words = 0
    from string import ascii_letters
    stringextra = ascii_letters + '-'
    noword = False
    for i in file1:
        if noword:
            if i not in stringextra:
                noword = False
        else:
            if i in stringextra:
                noword = True
                words = words+1

print('行数为%15s' %lines)
print('单词数为%13s' %words)
print('总字符数为%11s' %characters)
print("")


#第二题：求字母总数及每一字母出现的频率（不分大小写，按由高到低排序）
def processLine(line,CharacterCounts):
    for character in line:
        if ord(character) in range(97,123):
            CharacterCounts[character] += 1

def createCharacterCounts(CharacterCounts):
    for i in range(97,123):
        CharacterCounts[chr(i)] = 0

filename = "bill.txt"
infile = open(filename,"r")
CharacterCounts = {}
createCharacterCounts(CharacterCounts)
for line in infile:
    processLine(line.lower(),CharacterCounts)

pairs = list(CharacterCounts.items())
items = [[x,y]for (y,x)in pairs]
items.sort(reverse = True)

alls = 0
for i in range(len(items)):
    alls = alls + items[i][0]

print("文件中字母总数为%11d" %(alls))
print("")
    
for i in range(len(items)):
    print("出现字母%s的概率为%9.5f%%" %(items[i][1],((items[i][0])*100/alls)))
    
infile.close()


#第三题：求删去部分虚词后出现次数最多的十个单词
from collections import Counter
with open ("bill.txt","r",encoding = "utf-8") as fd:
    texts = fd.read()  
    texts.replace("-\r\n","")
    #构建要删除的单词列表
    delete_list = ["the","I","that","s","hath","He","OF","say","And","not","me","it","with","are","then","are","for","was","which","would","thy","ll","now","at","come","your","did","will","all","what","if","we","no","more","or","o","our","thou","they","from","so","To","do","shall","by","on","be","this","have","him","as","The","so","but","and","to","of","a","is","my","you","for","your","be","this","am","here","there","their","how","let","when","them","an","than","may","one","upon","have","him","as","The","so","but","and","O","That","But","You","My","What","Enter","A","If","us","For","to","of","a","is","my","you","in","d","he","his","she","her"]
    count = Counter(re.split(r"\W+", texts))
    for item in delete_list:
        del count[item]

result = count.most_common(10)
for i in range (len(result)):
    print ("文件中出现第%2.2s多的单词是%6s，出现了%2s次"%(i+1,result[i][0],result[i][1]))


