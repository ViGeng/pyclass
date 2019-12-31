#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


import re


exclulist = ['the', 'and', 'i', 'to', 'of', 'my', 'in', 'you',\
             'that', 'for', 'with', 'a', 'is', 'not', 'your', \
             'his', 'be', 'as', 'but', 'he', 'this', 'it', 'have',\
             'thou', 'me', 'will', 'by', 'so', 'thy', 'what', 'll', \
             'are', 'if', 'shall', 'do', 'we', 'him', 'or', 'our',\
             'her', 'no', 'on', 'from', 'at', 'they', 'would',\
             'which', 'was', 'their', 'she', 'am', 'how', 'when', \
             'than', 'an', 'more', 'thee', 'may', "i'll", 'upon', \
             'then', 'should', 'were', 'did', 'one', 'must', 'had', \
             'there', 'here', 'them', 'yet', 'these', 'sir', 'all',\
             'o', 'now']


def detect(text):
    encodings = 'ASCII', 'UTF-8', 'GBK'
    for encoding in encodings:
        try:
            with open(text, encoding = encoding) as f:
                f.read(100)
            break
        except UnicodeDecodeError:
            pass
    return encoding


def main():
    text = 'bill.txt'
    letter = 0
    line = 0
    word = 0
    count = 0
    list_ = []
    wordlist = dict()

            
    with open(text, mode = 'r', encoding = detect(text)) as file:
        for i in range(26):
            list_.append(0)

        f = file.read()
        line = f.count('\n') +1
        f = f.replace('-\n\n', '')

        
        for lines in f.splitlines(keepends = True):
            letter += len(lines)
            
            if len(lines)== 0:
                continue
            
            for i in range(len(lines)):
                if 'A' <= lines[i] <= 'Z':
                    list_[ord(lines[i])-65] += 1
                    count += 1
                if 'a' <= lines[i] <= 'z':
                    list_[ord(lines[i])-97] += 1    
                    count += 1
                
            for words in re.findall(r'\b\w{2,}\b', lines):
                word += 1
                if words.lower() in exclulist:
                    continue
                else:
                    wordlist[words.lower()] = wordlist.get(words.lower(), 0) + 1
                        

        print('文本中有%d个字符' % letter)
        print('文本中有%d行' % line)
        print('文本中有%d个单词' % word)


        for i in range(26):
            print('%s或%s出现的频率是%.4f' % (chr(i+65), chr(i+97), 100*list_[i]/count), '%', sep='')


        d = dict()
        d = sorted(wordlist.items(), key = lambda item:item[1], reverse = True)

        for i in range(10):
            print('频率第%d的单词是%s，出现次数为%d' % (i+1, d[i][0], wordlist[d[i][0]]))
            

if __name__ == '__main__':
    main()
