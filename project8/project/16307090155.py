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
#split函数
    
    text2 = text.split('\n')
    

#去除后面的空格（rstrip函数，其他去除空格的函数）
    for i in range(0,len(text2)):
        text2[i] = text2[i].rstrip()


#求最长一行的长度
    max_length = len(max(text2,key = len))
            
#上面的修饰栏
    head = '+' + '-'*(max_length) + '+'
    print(head)
    
    for line in text2[:-1]:
        print('|'+line+(max_length-len(line))*' '+'|')
    print(head)
    
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
    print(text)
    decorate_text(text)






    
