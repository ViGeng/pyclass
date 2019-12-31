import string
import re

with open('bill.txt','r') as f:
    #计算该文本包括空白字符在内总共有多少字符
    a = f.read()
    len(a)
    print('文本中包含%d字符（也包括那些空白字符）'%(len(a)))

    #计算该文本的行数
    b = a.splitlines()
    len(b)
    print('文本共包含%d行'%(len(b)))
    
    #计算该文本包含的单词数目，处理行尾单词折行问题
    c = a.strip('- \n')
    d = c.replace(',', ' ').split()
    len(d)
    print('文本共包含%d个单词'%(len(d)))

    print(40 * '-')
    
    #用循环实现文本中各字母（不区分大小写）出现的频率
    e = a.lower()
    dict_letter = {}
    for i in e:
        if ord('a') <= ord(i) <= ord('z'):
            dict_letter.setdefault(i,0)
            dict_letter[i] += 1
        else:
            pass
    x = sum(dict_letter.values()) 
    for key in dict_letter.keys():
        y = dict_letter[key]
        print('字母%s出现的频率为%7.3f%%' %(key,y/x*100))
        
    print(40 * '-')
    
    #找出文件中出现频率最高的10个单词
    text = e
    regexp = re.compile(r'\b\w+\b')
    word_list = []
    pos = 0
    while True:
        match = regexp.search(text,pos)
        if not match:
            break
        word_list.append(match.group())
        pos = match.end()
        
    word_number = len(d)
    
    count_word = {}
    for word in word_list:
        count_word.setdefault(word,0)
        count_word[word] += 1
        
    #创建排词表    
    exclude_words = ['the', 'and', 'i', 'to', 'of', 'a', 'you', 'my', 'that', 'in', 'is', 'd', 'not', 'for', 'with', 'me',
                    'it', 's', 'be', 'this', 'your', 'his', 'he', 'but', 'as', 'have', 'thou', 'so', 'him', 'will', 'what',
                    'by', 'thy', 'all', 'are', 'her', 'do', 'no', 'we', 'shall', 'if', 'on', 'or', 'thee',  'our', 'o', 'from',
                    'at', 'they', 'she', 'll','let', 'here', 'which', 'would', 'more', 'was', 'then', 'there', 'how', 'am', 
                    'their', 'when', 'them', 'an', 'may','than']
    for i in exclude_words:
        count_word.pop(i)
        
    z = sorted(count_word.items(), key = lambda item:item[1])
    z.reverse()
    i = 1
    while i <= 10:
        print('%2d.单词%-8s出现的次数为%6d，出现的频率为%10.6f%%'%(i,z[i-1][0],z[i-1][1],z[i-1][1]/word_number*100))
        i += 1
    
        
    

   
            
       
    
            
        
    


        
