t=""
with open("bill.txt","r",encoding="utf-8") as f:
    t=f.read().lower()
    
#字符数
zifu=len(t)
print('字符数为',zifu)

#行数
line=len(open("bill.txt",'r').readlines())
print('行数为',line)

#单词数统计
import re
sepword=re.findall('\\b[a-zA-Z]+\-\n',t)#找出所有折尾词
sepwordcount=len(sepword)#统计折尾词
t=re.sub('[^a-zA-Z]',' ',t)#用空格替换所有非字母
t1=re.sub('( )+',' ',t)#用单个空格替换多个空格
ts=t1.split(' ')#通过单词间空格分词
wordcount=len(ts)-sepwordcount#单词数（不包括数字和折尾词）统计
print('单词数为',wordcount)

#字母出现频率
print()
print('各字母出现频率如下：')
import string
t2=t.replace(' ','')#清除所有空格
t3=t2.replace('-','')#清除所有横杠
letterlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for m in range(26):    
    x=t3.count(letterlist[m])#每个字母出现次数
    y=len(t3)#总字母数
    letterpercent=x/y*100#字母出现频率百分比
    print(letterlist[m],'出现的频率为',letterpercent,'%',sep='')
    m=m+1

#单词词频前十位统计
print()
stopword={'between', 'only', 'his', 've', 'mightn', 'here', 'having', "you've", 'as', 'with', 'did', 'few', 'further', 'herself', 'their', "mustn't", "shouldn't", "she's", 'shan', 'myself', "haven't", 'an', 'your', 'above', 'its', 'has', "won't", 'haven', 'now', 'mustn', 'why', "it's", 'under', "you'd", 'off', 'after', 'own', 're', 'himself', 'but', "mightn't", 'of', 'aren', 'again', 'hadn', "needn't", "wouldn't", 'can', 'weren', "don't", 'will', "you'll", 'there', 'both', 's', 'over', 'up', 'isn', "you're", 'what', 'through', 'they', 'each', 'be', 'are', 'my', 'we', "that'll", 'than', 'most', 'had', 'nor', 'on', 'too', 'before', 'all', 'doesn', 'those', 'these', "isn't", 'do', 'whom', 'where', 'itself', 'am', 'i', 'themselves', 'by', 'such', 't', 'ain', 'needn', 'won', 'wasn', 'because', 'a', 'how', 'it', 'for', 'while', 'our', 'same', 'theirs', 'from', 'ourselves', 'about', 'shouldn', 'when', 'until', 'below', 'them', 'more', 'didn', 'to', 'some', 'were', 'no', "hadn't", 'or', "wasn't", "should've", 'ours', "couldn't", 'this', 'hers', 'into', 'does', 'll', 'couldn', 'once', 'have', 'y', 'not', 'she', 'should', 'm', 'being', 'which', 'doing', 'o', "doesn't", 'so', 'ma', 'me', 'is', 'down', 'who', 'yourselves', 'that', 'very', 'her', 'him', 'the', 'in', 'hasn', 'just', 'he', "didn't", 'during', "shan't", 'd', 'against', 'wouldn', 'don', 'then', 'any', "hasn't", 'at', 'yourself', 'if', 'out', 'and', 'was', 'been', "weren't", 'you', 'yours', "aren't", 'other'}
wordfre=[]
for i in stopword:
    wordcount=ts.count(i)#单词出现次数
    wordfre.append((i,wordcount))
wordfre=sorted(wordfre,key=lambda d:d[1],reverse=True)#以出现次数降序排序
wordfreten=wordfre[0:10]#降序前十
print('出现频率前十位的单词及次数如下：')
for (i,wordcount) in wordfreten:
    print('单词%s出现%s次'%(i,wordcount))

    
