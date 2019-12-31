import re
####统计单个字符的情况：
def count_character(txt):
    stat = {}#建立字典存储存储字符和对应频率
    stat1={}
    row=0 #w文章的行数
    for line in txt:
        row+=1
        line = line.strip()
        if len(line) == 0:
            continue
        for i in range(len(line)):
            #判断有无该字符的键
            if(line[i].lower() in stat):
                stat[line[i].lower()]+=1
            else:
                stat[line[i].lower()]=1
    result1=sorted(stat.items(),key = lambda x:x[0],reverse = True)#按value大小排序
    sum0=sum(stat.values())
    return result1,row,sum0,stat
bill = open('bill.txt' ,'r',encoding = 'utf-8')#读文件
r=count_character(bill)#调用函数
print("字符数量：",r[2])
print("行数量：",r[1])
for t in r[3].items():
    if 'a'<=t[0]<='z':
        print("%s的出现的频率为："%t[0],t[1]/r[2] )
bill.close
#####统计单词的情况
f =open('bill.txt' ,'r',encoding = 'utf-8')
word_dict = {} # 用于统计 word：个数
word_list = [] # 用于存放所有单词
for line in f.readlines():
    for word in line.strip().split(" "):
        word_list.append(re.sub(r"[^a-zA-Z]", "", word.lower()))
print("单词数量为：",len(word_list))
word_sets = list(set(word_list))   # 确保唯一
word_dict = {word: word_list.count(word) for word in word_sets if word}
#result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:20]
ignore_list=['the','i','of','a','and','to','of','you','my','that','in','is','not','for','with','me','it','be','this','your','his']
for key in ignore_list:
    if key in word_dict.keys():
        del word_dict[key]
result1 = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:10]
print(result1)