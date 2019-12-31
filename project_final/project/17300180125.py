import string
def count_characters():
    #计算文本中的字符数（包含空白字符）
    charc=0
    for i in string.printable:
        charc+=s0.count(i)
    return charc

def count_lines():
    #计算文本中的行数
    L=s.splitlines()
    l=int(len(L))
    return l

def count_words():
    """计算文本中的单词数目,其中有连字符的已作处理，缩略形式如I'm算作一个单词，
    详细注解写在下一函数中，步骤相同"""
    L1=[]
    linelist=[]
    for line in s4.splitlines():
        if line=='':
            continue
        else:
            linelist.append(line.strip())
            
    for i in range(len(linelist)):
        if linelist[i].endswith(('-')):
            L=linelist[i].split(sep=None,maxsplit=-1)
            newL=linelist[i+1].split(sep=None,maxsplit=-1)
            L.append(L[int(len(L))-1].rstrip('-')+newL[0])
            del L[int(len(L))-2]
            for j in range(int(len(L))):
                L1.append(L[j])
            
        elif linelist[i-1].endswith(('-')):
             L=linelist[i].split(sep=None,maxsplit=-1)
             for j in range(1,int(len(L))):
                L1.append(L[j])
        else:
            L=linelist[i].split(sep=None,maxsplit=-1)
            for j in range(int(len(L))):
                L1.append(L[j])
    words=len(L1)
    return words
   

def count_alphabet():
    #计算各个字母在文中出现的频率
    countalpha={}
    alphabet=list(string.ascii_lowercase)
    for i in range(26):
        countalpha[alphabet[i]]=0
        
    for ch in s3 :
        if ch.isalpha():
            countalpha[ch]+=1
    #用字典记录各个单词出现的次数，再计算频率
    total=0
    for i in range(26):
        total+=countalpha[alphabet[i]]
        
    for i in range(26):
        a1=countalpha[alphabet[i]]/total
        print("字母",alphabet[i],"出现的频率为",'%.2f%%'%(a1*100))
        
def select_words():
    L1=[]
    Number={}
    linelist=[]
    for line in s4.splitlines():
        if line=='':
            continue
        else:
            linelist.append(line.strip())
            
    for i in range(len(linelist)):
        if linelist[i].endswith(('-')):
            L=linelist[i].split(sep=None,maxsplit=-1)
            newL=linelist[i+1].split(sep=None,maxsplit=-1)
            L.append(L[int(len(L))-1].rstrip('-')+newL[0])
            del L[int(len(L))-2]
            for j in range(int(len(L))):
                L1.append(L[j])
    #对换行单词进行处理，将其和下一行的部分拼接起来     
        elif linelist[i-1].endswith(('-')):
             L=linelist[i].split(sep=None,maxsplit=-1)
             for j in range(1,int(len(L))):
                L1.append(L[j])
    #被拼接的那一行从列表1号位元素开始增加单词
        else:
            L=linelist[i].split(sep=None,maxsplit=-1)
            for j in range(int(len(L))):
                L1.append(L[j])
    #把分割出来的单词都放进列表里
                
    allwords=set(L1)
    #转换为集合可以删去重复的元素
    
    for word in allwords:
        Number[word]=0
    #建立字典

    for word in L1:
        Number[word]+=1
    #通过单词在列表里出现的指标数的个数计算其出现次数
   
    print('%-s'%"要剔除的单词有：")
    for word in allwords:
        if int(Number[word])>3200 :
            print('%-15s' '%5s' '%5s'%(word,"出现次数为",Number[word]))
            del Number[word]
    #剔除出现次数过多的介词等
        elif word in (  'would' ,'am','o','they','them','she','he','our','more','many',
                        'much','than','then','hath','a','an','with','tis','is','was','on',
                        'or','thee','at','from','how','which','why','here','there') :
            print('%-15s' '%5s' '%5s'%(word,"出现次数为",Number[word]))
            del Number[word]
    #剔除无很大意义的介词副词及其缩写

    
    print('-'*40)
    newlist=sorted(Number.items(),key=lambda item:item[1],reverse=True)[:10]
    print('%-s'%"文中除去被排除的单词外出现次数最高的十个单词为：")
    for i in range(10):
        print('%-15s' '%5s' '%5s'%(newlist[i][0],"出现次数为",newlist[i][1]))


if __name__=='__main__':
    f=open('bill.txt','r')
    s0=f.read()
    s=s0.strip()
    s3=s.lower()
    #处理成小写方便统计字母出现频率和单词出现频率
    mostsigns1=string.punctuation.replace('-','')
    mostsigns=string.punctuation.replace('\'','')
    table1=str.maketrans(mostsigns,' '*int(len(string.punctuation)-1))
    s4=s3.translate(table1)
    '''这几行的意义在于保留连字符和单引号（因为连字符有意义需单独处理，
    而文中的单引号多为缩写或者surpris'd这种用来代替e的用法，所以保留，将缩写形式视为一个词），
    而将其他标点符号替换为空白'''
    
    l=count_lines()
    print("莎士比亚文选中一共有",l,"行")
    c=count_characters()
    print("莎士比亚文选中一共有",c,"个字符")
    n=count_words()
    print("莎士比亚文选中一共有",n,"个单词")
    print('-'*40) 
    count_alphabet()
    print('-'*40)
    
    select_words()
    f.close()
    #关闭文件
