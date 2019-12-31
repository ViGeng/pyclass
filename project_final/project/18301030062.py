#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

"读取文本"
txt = open("bill.txt","r").read()
txt = txt.lower()

"计算字符个数"
txt1 = txt.replace('\n','')
totalnum = 0
for charac in txt1:
    if not charac.isspace():
        totalnum += 1
print('字符个数为', totalnum)

"计算行数"
txt2 = txt.splitlines()
linenum = 0
for line in txt1:
    if line.strip() != '':
        linenum += 1
print('行数为', linenum)

"计算单词个数，找到出现次数最多的10个单词及其出现的次数"
for ch in '!"#$%&()*+,-./:;<=>?@[\]^_{|}~':
    txt3 = txt.replace(ch,' ')
words = txt3.split()
counts = {}
wordnum = 0
for word in words:
    wordnum += 1
    counts[word] = counts.get(word,0) + 1
print('单词个数为', wordnum)

items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
print()
print('出现次数最多的10个单词：')
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
        
"找到各单词出现的频率"
letters = {}
for charac in txt1:
    if charac.isalpha():
       letters[charac] = counts.get(charac,0) + 1
letters_fre = list(letters.items())
letters_fre.sort(key = lambda x:x[0])              
fre_total = 0
for letter in letters_fre:
    fre_total += letter[1]
for letter in letters_fre:
    abc = letter[0]
    abc_fre = letter[1] / fre_total
    print('%s出现的频率是%s' % (abc,abc_fre))
    
        
    
    
    
    
