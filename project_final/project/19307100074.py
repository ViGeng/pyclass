import os
import string
import re
from operator import itemgetter

with open('bill.txt') as f:
    s= f.readlines()
    quan=0
    for i in s:
        quan+=len(i)
    print('字符数',quan)
    lines = len(s)
    print('行数',lines)
    words=0
    special=0
    for i in s:
        words+=len((i.strip()).split())
        if i.endswith('-\n'):
            words+=-1
    print('单词数',words)

with open('bill.txt') as f:
    text = f.read()
    letter=0
    for w in text:
        if w in string.ascii_letters:
            letter+=1
    for add in range(26):
        rate =(text.count(chr(65+add))+text.count(chr(97+add)))/letter
        print('文件中',chr(65+add),'（不区分大小写）出现的频率（所占百分比）'+str('%.3f'%(100*rate))+'%')

with open('bill.txt') as f2:
    text_= f2.read()
    pattern=r'-.*?\\n.*?\\n'
    text = re.sub(pattern,'',text_)
    box = text.split()
    num={}
    for word in box:
        num[word.lower()] = num.get(word.lower(),0)+1
new=sorted(num.items(),key=itemgetter(1),reverse=True)
a=0
b=0
nono=['the','and','to','of','a','in','for','with','not','thou','by','so','thy','or','no','on','from','at',]
while 10-a:
    if new[b][0] in nono:
        b+=1
        continue
    else:
        a+=1
        print('频率第','%-4d'%a,'的单词是',new[b][0],'出现了',new[b][1],'次')
        b+=1
        

