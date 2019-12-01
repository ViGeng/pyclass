#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def decorate_text(text):
    '''
    有一段英文文本（这样我们不用考虑中文文本导致的对齐问题），该文本有多行，每行前后可能会有空格，
    每行前面的空格要保留，而每行最后的空格应该去除。请在这段英文文本上面加上装饰栏。
    有一段英文文本（这样我们不用考虑中文文本导致的对齐问题），该文本有多行，每行前后可能会有空格，
    每行前面的空格要保留，而每行最后的空格应该去除。请在这段英文文本上面加上装饰栏，如下所示
+-------------------------------------------------------------------------------+
|  The King and Queen of Hearts were seated on their throne when they arrived,  |
|with a great crowd assembled about them--all sorts of little birds and beasts, |
|as well as the whole pack of cards: the Knave was standing before them, in     |
|chains, with a soldier on each side to guard him; and near the King was the    |
|White Rabbit, with a trumpet in one hand, and a scroll of parchment in the     |
|other. In the very middle of the court was a table, with a large dish of tarts |
|upon it: they looked so good, that it made Alice quite hungry to look at them--|
|`I wish they'd get the trial done,' she thought, `and hand round the           |
|refreshments!'                                                                 |
|                                                                               |
|  But there seemed to be no chance of this, so she began looking at everything |
|about her, to pass away the time.                                              |
|                                                                               |
+-------------------------------------------------------------------------------+
    '''
    lines_number = text.count('\n') + (text[-1]!= '\n') #统计字符串行数，包括最后一行
    length_list = []
    text_split = text.splitlines()#把文章分行
    for i in range((lines_number-1)):
        each_line = text_split[i]#给每一行编号
        each_line_split = each_line.split()#把每行的单词分出来
        each_line_join = '+'.join(each_line_split)#联结每个单词，用加号替代空格
        each_line_count = each_line_join.count('')#根据每个字母之间的空格，算出整句话的长度，但是会+1
        length_list_append = length_list.append([each_line_count])
        pass
    max_length = length_list[0]
    for i in range(len(length_list)):#选出最长的一行
        if length_list[i] > max_length:
            max_length = length_list[i]
            pass
    max_length = max_length[0]

    s = '++'
    p = '||'
    first_last_line = ('-'*(max_length-1)).join(s)#可以设定长度，然后join
    print(first_last_line)
    for i in range((lines_number)):
        each_line = text_split[i]
        each_line_0 = each_line.rstrip()
        each_line_1 = each_line_0.ljust((max_length-1))
        line_decoration = (each_line_1).join(p)
        print(line_decoration)
    print(first_last_line)
    pass


if __name__ == '__main__':
    print('-'*40)
    print('将输入的文本加上装饰条') 

    text = r'''  The King and Queen of Hearts were seated on their throne when they arrived,      
with a great crowd assembled about them--all sorts of little birds and beasts,   
as well as the whole pack of cards: the Knave was standing before them, in  
chains, with a soldier on each side to guard him; and near the King was the    
White Rabbit, with a trumpet in one hand, and a scroll of parchment in the     
other. In the very middle of the court was a table, with a large dish of tarts            
upon it: they looked so good, that it made Alice quite hungry to look at them--   
`I wish they'd get the trial done,' she thought, `and hand round the     
refreshments!'

  But there seemed to be no chance of this, so she began looking at everything           
about her, to pass away the time.         
    '''
    decorate_text(text)
    
