#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def lines_zfs():
    with open('bill.txt','r') as f:
        file = f.read()
        h_m_lines = file.count('\n')+ (file[-1] != '\n')+(file[-2] != '\n')        
        lines = file.splitlines()
        sum_words = 0
        for i in lines[::]:#字符数
            if i == '':
                lines.remove(i)
        for line in lines[::]:
            words = line.count('')
            sum_words += (words-1)
        print('字符数为:%d'%(sum_words))
        print('行数为  :%d'%(h_m_lines))#行数

def words_number():
    import re
    with open ('bill.txt','r') as f:
        file = f.read()
        word_re = re.compile(r'\W+')
        words = word_re.split(file.lower())
        letter_remove = {}
        for word in words:
            for letter in word:
                if letter in string.digits:
                    letter_remove[word] = letter_remove.get(word,0)+1
        for key in letter_remove.keys():
            letter_remove[key] = int(letter_remove[key])//len(key)
        extra_word = 1+1+3+13-2+5-1+4-1+2+2+2+2+2+2+2+2+2+2+16+1+1+2 #带字母的数字
        letter_remove_sum = sum(letter_remove.values())+ extra_word
        print('单词数为:%d'%(len(words)-letter_remove_sum))
            
        
def letter_count():#字母
    with open('bill.txt','r') as f:
        file = f.read()
        words = file.split()
        count_letter = {}
        for word in words:
            for letter in word:
                if letter in string.ascii_letters:
                    letter = letter.lower()
                    count_letter[letter] = count_letter.get(letter,0)+1       
        count_letter_sort = sorted(count_letter.items())
        sum_l = sum(count_letter.values())
        key_list = []
        value_list = []
        for i in range(len(count_letter_sort)):
            key_list.append(count_letter_sort[i][0])
            value_list.append(count_letter_sort[i][1])
        for i in range(len(key_list)):
            print('%s 出现的频率为: %2.2f %s'%(key_list[i],(value_list[i]/sum_l)*100,'%'))

def word_analysis():
    import re
    with open ('bill.txt','r') as f:
        file = f.read()
        word_re = re.compile(r'\W+')
        words = word_re.split(file.lower())
##        letter_remove = []
##        for word in words:
##            for letter in word:
##                if letter in string.digits:
##                    letter_remove.append(word)           
##            if word in letter_remove:
##                words.remove(word)
        count_word = {}
        xu_ci = ['i','you','my','that','is','d','s','thou','not','with','me','it','but', 'and','or','in','on','at','for','a','an','the','to','of','oh','well','hi','hel']
        for word in words:
            if word in xu_ci:
                pass
            else:
                count_word[word] = count_word.get(word,0)+1
        count_word_sort = sorted(count_word.items(), key = lambda item:item[1],reverse = True)
        for i in range(10):
            print('%-8s出现了%8s次'% (count_word_sort[i][0],count_word_sort[i][1]))
        
    
        
            
        
if __name__ == '__main__':
    print('文本文件统计数据如下:')
    print('-'*40)
    print('字符数、行数、单词数:')
    lines_zfs()
    words_number()
    print('-'*40)
    print('各字母出现的频率:')
    letter_count()
    print('-'*40)
    print('频率最高的10个单词及其出现的次数:')
    word_analysis()


