#!/usr/bin/env python
# coding: utf-8
'''
    要求计算并打印有关文本文件内容的统计数据。包括:
    1.用户指定的文本文件中，包含多少字符(也包括那些空白字符)、多少行、 多少单词(注意行尾单词折行的问题,这种情况通常行尾会有连字号-)。
    2.文件中各字母(不区分大小写)出现的频率(所占百分比)。
    3.文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一-些the这样的虚词，你也可以创建一个排除词的列表 ，其中包含要忽略的所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
    
    测试数据是莎士比亚全集，"bill.txt"文件， 文件大小5.6M字节。
'''

#导入模块
import time
import re

def Statistical_poetry():
    #读取文件
    with open('bill.txt', 'r') as f:
        str = f.read()


    # ## 获得所有的字符和换行符

    format_str = str.lower()

    char_list = format_str
    char_dict = {}
    num_line = 1
    for c in char_list:
        if c == '\n': # 这里不能使用r'\n'强转义，因为本来需要判断的就是换行符
            num_line += 1
        elif c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    # 把字典按value降序排列
    char_sort = sorted(char_dict.items(), key = lambda x:x[1], reverse=True)
    #字符出现频数
    print("\n字符出现频数\n",char_dict)
    #字符统计
    num_char = sum(x[1]  for x in char_sort)
    print("\n字符统计:\n",num_char)
    #行数统计
    print('\n行数统计:\n',num_line)

    #re.findall('(-[\n]+)', 'bb-\n\na')
    #re.findall('[a-z]\'ned','threat\'ned')
    #k = re.sub('([a-z]+)(\'ned)',lambda m:m.group(1)+'ened',"threat'ned happ'ned 'neddd'")
    #kk = re.findall("[a-z]+'{0,1}[a-z]+","threat'ned happ'ned 'neddd'   :'asas'")

    #单词统计

    '''
    situation 1//
        考虑行尾单词折行:
        会出现：
        con-
        
        e(即con-\n...\ne)
    situation 2//
        英文诗歌会因为凑音节的缘故而省去单个字母,然后用撇代替
        1、单词“over”可以简写成“o'er”
        2、“threatened”、“happened”、“softened”、“lengthened”、“lessened”、“christened”...等ened结尾的单词替换成以'end结尾
        替换成“threat'ned”、“happ'ned”、“soft'ned”...
        3、“finished”、“loved”、“inclined”、“curled”...等ed结尾的单词被替换成了“furnish'd”、“lov'd”、“inclin'd”、“curl'd”
    situation 3//
        1、单词“O”是语气词“OH”的简写 
        2、'tis 在古语、诗歌中使用，意思是 it is ||| 'em 表示 them
        3、古体英语诗句中动词+'st ，表示第二人称
        4、on't、in't、to't、for't 分别表示 on it 、in it、to it 、for it 
    '''
    str_no_fl = re.sub('(-[\n]+)', '', format_str)
    #str_no_fl = re.sub('o\'er','over',str_no_fl)#还原单词over
    #str_no_fl = re.sub('([a-z]+)(\'ned)',lambda m:m.group(1)+'ened',str_no_fl)#还原以ened结尾的单词
    #str_no_fl = re.sub('([a-z]{2,})(\'d)',lambda m:m.group(1)+'ed',str_no_fl)#还原以ed结尾的单词,i'd除外

    # 获得单词列表
    word_list = re.findall(r"[a-z]+'{0,1}[a-z]+", str_no_fl)
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    word_dict
    len(word_list)

    # 把字典按value降序排列
    word_sort = sorted(word_dict.items(),key=lambda x:x[1], reverse=True)
    # 统计单词个数
    num_word = sum(x[1]  for x in word_sort)
    print('\n统计单词个数:\n',num_word)

    #单词出现频率
    print('\n单词出现频率:\n',word_sort)
    #出现频数最高的十个单词
    top_10_words = word_sort[0:10]
    print('\n出现频数最高的十个单词')
    for a,b in enumerate(top_10_words,1):
        print('[{0:<2}]  {1}'.format(a,b))


    #creat exclusion word list (including some common function words)
    ex_words = ['the', 'a', 'in', 'on', 'and', 'but', 'at', 'for', 'an', 'from', 'behind', 'above', 'of', 'to']
    new_words_rank = []
    number = 0
    key = True
    for word in word_sort:
        if number == 10:
            break
        #print(word)
        for ex_word in ex_words:
            if ex_word == word[0]:
                key = False
        if key == True:
            number += 1 
            new_words_rank.append(word)
        key = True
    print('\n排除词之外的出现频数最高的10个单词:')
    for a,b in enumerate(new_words_rank,1):
        print('[{0:<2}]  {1}'.format(a,b))
    return char_dict, num_char, num_line, num_word, word_sort, top_10_words, new_words_rank

if __name__=="__main__":
    Statistical_poetry()






