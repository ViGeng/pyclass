#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import re
import string

def main():
    with open('bill.txt') as file:
        textlist = file.readlines()
        textstr = ''.join(textlist)
        regexp = re.compile(r'(\w*)-\n\n') #去除行尾的连字符以及之后的两个换行符，如果是真正的连字符原本被连字符隔开的两部分会合并到一起，不表示连字符的‘-’这样操作不会对单词个数造成影响
        textstr = regexp.sub(r'\1',textstr)

    total_character = 0
    for line in textlist:
        total_character += len(line)

    print('文本共有',total_character,'个字符',sep = '')
    print('文本共有',len(textlist),'行',sep = '')
    print('文本共有',len(textstr.split()),'个单词',sep = '') #用split，按照空格分割单词
    print()

    letter_dict = dict() #初始化字典

    for line in textlist:
        lower_line = line.lower()
        for i in lower_line:
            if i in string.ascii_lowercase:
                if i in letter_dict:
                    letter_dict[i] += 1
                else:
                    letter_dict[i] = 1

    for letter in string.ascii_lowercase:
        total_letter = sum(letter_dict.values())
        print('%s%s%8.3f%s'%(letter,'(不区分大小写)的出现频率:',100 * letter_dict[letter] / total_letter,'%'))

    words_list = [word.strip(string.punctuation).lower() for word in textstr.split()] #去除标点符号

    words_dict = dict() #初始化字典
    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    print()
    exclude = input('请输入排除词，两个单词之间用空格隔开:')
    exclude = exclude.lower()
    for key in words_dict.copy():
        if key in exclude.split():
            del words_dict[key]

    sorted_list = sorted(words_dict.items(),key = lambda item:item[1],reverse = True)[:10]
    print('排除词以外出现频率最高的10个单词:')
    print('%s %-10s%10s'%('排序','单词','次数'))
    times = 0
    for item in sorted_list:
        times += 1
        print('%3d  %-10s %13d'%(times,item[0],item[1]))

if __name__ == '__main__':
    main()

