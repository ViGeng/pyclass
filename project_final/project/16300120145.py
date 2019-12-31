import re
import string

def get_data():
    content = open("bill.txt").read()
    content = content.lower()
    words = content.split()
    num_chr = len(content)
    num_lines = content.count('\n')
    count = 0
    for line in content:
        if line.endswith('-'):
            count += 1
    num_words = len(words) - count
    
    for i in string.ascii_lowercase:
        items = re.findall(i,content,re.I)
        letter = (len(items)/num_chr)*100
        print('莎士比亚全集中字母%s出现的频率为%.3f%%'%(i,letter))
    
    print('-'*40)    
    print('莎士比亚全集中有%d个字符'%num_chr)
    print('莎士比亚全集中有%d行'%num_lines)
    print('莎士比亚全集中有%d个单词'%num_words)

def get_data1():
    txt=open("bill.txt").read()
    txt=txt.lower()
    for ch in '!"$+&,/=@{}[]\\?.-':
        txt = txt.replace(ch,"")
    return txt

Shakespeare=get_data1()
billtxt = Shakespeare.split()
counts={}
for word in billtxt:
    if word in ('the','and','to','of','a','that','in','for','with'):
        word.strip()
    else:
        counts[word]=counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

print('-'*40)

if __name__ == '__main__':
    get_data()
    get_data1()


'''
1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、
多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。

2。文件中各字母（不区分大小写）出现的频率（所占百分比）。

3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是
一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的所有
单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
'''
