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
    '''想法
    1）按行分隔，去除末尾空格，统计各行长度
    2）按最长的单行长度格式化，最前面加丨，最后面加丨，固定长度为max_length    #列表解析式 max语句
    3）头尾加装饰栏'''                                                           #填充

    text_lines = text.splitlines()          #按行分隔

    text_lines_2 = []                         #去除行末空格
    for line in text_lines:
        line_2 = line.rstrip()
        text_lines_2.append(line_2)

    line_length = []                         #统计各行长度
    [line_length.append(len(line_2)) for line_2 in text_lines_2]
    max_length = max(line_length)               #最长行

    new_text = []                              #格式化
    for new_line in text_lines_2:
        new_line = '{0: <{1}}'.format(new_line, max_length)   #格式化结果记得存储！！！｛嵌套，动态格式化｝
        new_line_2 = '|%s|' % new_line
        new_text.append(new_line_2)


    print('+'+'-'*max_length+'+')
    [print(new_line) for new_line in new_text]
    print('+' + '-'*max_length + '+')

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

