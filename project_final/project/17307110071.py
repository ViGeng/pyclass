#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import re
import string


def statistic(file):
    '''
    统计文本文档file的信息，打印出file的字符数，行数，单词数，各字母出现的频率，以及出现频率最高的10个单词，
    由于介词等词汇太多无法全部包含，这里只在统计时忽略处理字符串时出现的单个字母的单词以及一些平凡的单词，
    可以选择是否打印所有单词的出现次数(包含上述被忽略的）,y表示打印，其余表示退出。
    忽略词如下['i', 'me', 'my', 'mine', 'myself', 'you', 'your', 
             'yours', 'yourself', 'he', 'him', 'his', 'himself',
             'she', 'her', 'hers', 'herself', 'it', 'its',
             'itself', 'we', 'us', 'our', 'ours', 'ours', 'ourselves',
             'yourselves', 'they', 'them', 'their', 'theirs',
             'themselves', 'can', 'could', 'may', 'might', 'must',
             'will', 'would', 'shall', 'should', 'ought', 'have',
             'rather', 'in', 'at', 'on', 'll', 'from', 'to', 'by', 'or',
             'and', 'is', 'was', 'were', 'of', 'that', 'not', 'for',
             'with', 'be', 'this', 'but', 'the', 'as', 'thou', 'so',
             'what', 'thy', 'all', 'are', 'do', 'no', 'if', 'thee',
             'which', 'here', 'there', 'let']
    包括单字母(未列出),人称代词,情态动词,和部分介词
    '''
    strict_line_num = 0  # 不计空行的行数
    all_letter = 0       # 字符总数
    word_count = 0       # 单词总数
    letter_stat = {}     # 字母统计
    word_stat = {}       # 单词统计
    is_hyphen = False    # 判断上一行末尾是否是连字符
    remain = ''          # 被连字符分割的单词的前半部分
    trivial_words = ['i', 'me', 'my', 'mine', 'myself', 'you', 'your',          # 忽略这些单词
                     'yours', 'yourself', 'he', 'him', 'his', 'himself',
                     'she', 'her', 'hers', 'herself', 'it', 'its',
                     'itself', 'we', 'us', 'our', 'ours', 'ours', 'ourselves',
                     'yourselves', 'they', 'them', 'their', 'theirs',
                     'themselves', 'can', 'could', 'may', 'might', 'must',
                     'will', 'would', 'shall', 'should', 'ought', 'have',
                     'rather', 'in', 'at', 'on', 'll', 'from', 'to', 'by', 'or',
                     'and', 'is', 'was', 'were', 'of', 'that', 'not', 'for',
                     'with', 'be', 'this', 'but', 'the', 'as', 'thou', 'so',
                     'what', 'thy', 'all', 'are', 'do', 'no', 'if', 'thee',
                     'which', 'here', 'there', 'let']
    trivial_words.extend(list(string.ascii_lowercase))  # 上述列表加入26个小写字母

    with open(file, 'r') as f:
        lines = f.readlines()

    raw_line_num = len(lines)  # 计空行的行数

    for line in lines:
        if line == '\n':
            continue
        else:
            strict_line_num += 1      # 非空行数加一
            all_letter += len(line)   # 把这行的字符数加入总字符数

            if is_hyphen:
                line = remain + line  # 若上一行末尾是连字符，则把上一行末尾接到这行的开头

            is_hyphen = (line[-2] == '-')  # 判断本行末尾是否是连字符

            line = re.sub(r'[^A-Za-z]+', ' ', line)  # 把非字母的字符替换成空格再split分离
            line = line.split()

            if is_hyphen:
                remain = line[-1]  # 若本行末尾是连字符则要从列表去掉最后被分割的单词
                line.pop()

            word_count += len(line)  # 计入本行的单词数

            for word in line:        # 统计本行的单词和字母，统一小写
                word = word.lower()
                if word in word_stat:
                    word_stat[word] += 1
                else:
                    word_stat[word] = 1
                for letter in word:
                    if letter in letter_stat:
                        letter_stat[letter] += 1
                    else:
                        letter_stat[letter] = 1

    word_stat = sorted(word_stat.items(),          # 按出现次数降序排列
                       key=lambda items: items[1],
                       reverse=True)

    count = 0   # 计算字母总数
    for key in letter_stat:
        count += letter_stat[key]
    letter_stat = sorted(letter_stat.items())  #字母统计按字母顺序排序

    # 打印部分
    print('统计文本 {} 的信息如下：'.format(file))

    print('')
    print('总字符数 ： 　  　 {}'.format(all_letter))
    print('总行数(计空行)：   {}'.format(raw_line_num))
    print('总行数(不计空行):  {}'.format(strict_line_num))
    print('单词数 :  　 　　　{}'.format(word_count))

    print('')
    print('各字母（不区分大小写）出现的频率为:')  # 打印各字母出现频率
    for item in letter_stat:
        print('{}: {:.2f}%'.format(item[0], int(item[1])*100/count))

    print('')
    print('出现最多的十个单词为：')  # 打印word_stat列表中不在trivial_words里的元素
    i = count = 0
    while True:
        if i == len(word_stat) or count == 10:  # 若已打印十个或已遍历列表则结束
            if count == 0:                      # 若列表中单词全部都是trivial_word,则打印提示
                print('文档中没有非平凡词汇！')
            break
        if word_stat[i][0] not in trivial_words:  #打印非平凡单词
            print('{:<20}{}'.format(word_stat[i][0], word_stat[i][1]))
            count += 1
        i += 1
        

    print('')
    x = input('是否显示所有单词的统计结果(输入y确认，其余退出）')
    if x == 'y':
        for i in range(len(word_stat)):
            print('{:<20}{}'.format(word_stat[i][0], word_stat[i][1]))


if __name__ == '__main__':
    statistic('bill.txt')
