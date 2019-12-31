import re
from collections import Counter

def question1():
    file1=open('bill.txt','r',encoding='utf-8')
    print('第一题')
    a=file1.read()
    a.lower()
    count=len(a)
    print('字符数：',count,end=' ')
    lines=len(a.split('\n'))
    print('行数：',lines,end=' ')
    word='[a-z]+'
    wordlist=re.findall(word,a)
    print('单词数：',len(wordlist))
    file1.close()

def question2():
    file2=open('bill.txt','r',encoding='utf-8')
    print('第二题')
    a=file2.read()
    a.lower()
    re=Counter(a)
    count={}
    sum1=0
    i=97
    while i<=122:
        a=chr(i)
        sum1+=re[a]
        i+=1
    i=97
    while i<=122:
        a=chr(i)
        count[a]=(re[a]/sum1*100)
        i+=1
    print('各字母出现频率：',count)
    file2.close()

def question3():
    worddic={}
    file3=open('bill.txt','r',encoding='utf-8')
    print('第三题')
    a=file3.read()
    a.lower()
    word='[a-z]+'
    wordlist=re.findall(word,a)
    for i in wordlist:
        if i not in worddic:
            worddic[i]=1
        else:
            worddic[i]+=1
    deletelist=['her','all','our','so','or','as','will','this','have','thou','the','my','you','and','d','i','y','of','at','on','to','your','a','in','is','that','not','me','s','with','it','his','him','for','with','it','he','nd','but']
    print('排除词列表：',deletelist)
    for i in deletelist:
        if i in worddic:
            del worddic[i]
    a=sorted(worddic.items(),key=lambda item:item[1],reverse=True)
    a=a[0:10]
    print('高频词：',a)
    file3.close()


        

    
    


def main():
    question1()
    question2()
    question3()

if __name__=='__main__':
    main()


