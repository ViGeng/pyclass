#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

'''
要求计算并打印有关文本文件内容的统计数据。包括：
1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。
2。文件中各字母（不区分大小写）出现的频率（所占百分比）。
3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的
所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
'''

def input_file(file_name):
    try:
        f = open(file_name, 'r')
    except IOError as E:
        print(E)
        return None
    
    line_number = 0
    for line in f:
        if not line.isspace():
            line_number += 1
    f.seek(0)
  
    try:
        text = f.read()
    except:
        print("Read File Error!")
        return None
    
    f.close()
    
    return text, line_number

def count_char(text):
    text = text.replace('\n', '').strip()
    char_number = len(text)
    
    char_freq = dict()
    text = text.lower()
    total = 0
    for ch in text:
        if ch not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        char_freq[ch] = char_freq.get(ch, 0) + 1
        total += 1
    for key in char_freq.keys():
        #print(key, ':', char_freq[key])
        char_freq[key] = char_freq[key] / total * 100
    char_freq = sorted(char_freq.items(), key=lambda v: v[1], reverse=True)
    
    return char_number, char_freq

def count_word(text):
    new_text = text.lower()
    new_text = new_text.replace('-\n', '')
    for ch in "~@#$%^&*()!_-+=<>?/,.:;{}[]|\'""":
        new_text = new_text.replace(ch, ' ')
    words = new_text.split()
    word_number = len(words)

    excludes = ['the','and','to','of','i','a','in','it','that','is',
            'you','my','with','not','his','this','but','for',
            'me','s','he','be','as','so','him','your','d']
    word_freq = dict()
    for word in words:
        if word in excludes:
            continue
        word_freq[word] = word_freq.get(word, 0) + 1
    word_freq = sorted(word_freq.items(), key=lambda v: v[1], reverse=True)
    
    return word_number, word_freq

def main():
    text, line_number = input_file('bill.txt')
    char_number, char_freq = count_char(text)
    word_number, word_freq = count_word(text)
    print("行数：", line_number)
    print("字符数：", char_number)
    print("字母出现的频率：")
    for item in char_freq:
        print("{0:}: {1:>2.2f} %".format(*item))
    print("单词数：", word_number)
    for item in word_freq[:10]:
        print("{0:}: {1:}".format(*item))

if __name__ == '__main__':
    main()
