import re , string
dic = {}
txt = open('bill.txt','r').read()
txt = txt.lower()
counts = {}
n = 0


# 字符(包括空白字符)、行数、单词数(注意行尾单词折行问题：行尾会有连字号‘-’)


mylen = len(txt)
line_num = txt.count("\n")
print ('字符数：%s \n行数：%s' %(mylen,line_num))


for line in txt:
    r = ('[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+')
    line = re.sub (r , '' , txt)
    line = re.sub (r'-' , '' , txt)
    for word in line.split():
        if word [-1] == '-':
            m = word [:-1]
            n = 1
            break
        elif n == 1:
            word = m + word
            n = 0
    word_num = len(line.split())
    print ('单词数：%s' %(word_num))
    dic.setdefault(word.lower(),0)
    dic[word.lower()] += 1
    break
print()


# 文字中各字母(不分大小写)出现的频率(所占百分比)


count_en = 0
for s in txt:
    if s in string.ascii_letters:
        count_en += 1
print ('纯英文字符：', count_en)

        
for i in txt:
    if i in string.ascii_letters:
        counts [i] = counts.get(i,0)+1
items = list (counts.items())
items.sort (key = lambda x:x[1] , reverse = True)


print ('%s %5s %6s' % ('字母', '出现次数', '出现频率'))
for i in range(len(items)):
    word,count = items[i]
    print ('{0:<5}{1:<10}{2:<5}'.format(word,count,'{:.2%}'.format(count/count_en)))
print()


# 出现频率最高的10个单词及它们出现的次数，可创建一个排除常出现的单(如:虚词等)的列表，其中包含要忽略的所有单词，统计列表以外的单词出现次数


unwanted = ['','a','an','the','will','shall','i','you','we','they','he','she','it','our','their','mine','yours','him','his','her','my','your','me','you','this','that','is','am','are','was','were','no','be','in','of','d','s','in','with','to','or','and','if','no']
d = {}
count = 0
with open('bill.txt','r')as f:
    for line in f:
        line = line.lower()
        words = re.split('\W|_',line)
        for word in filter(lambda word :word.lower() not in unwanted ,words): 
            d[word] = d.get(word,0)+1
            
print ('出现频率最高的10个单词与出现次数：')
print (sorted(d.items(),key = lambda x :x[1],reverse = True )[:10])


