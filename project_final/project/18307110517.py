import collections
import re
a = open(r"bill.txt",'r')
s = a.read()
s = s.lower()
zimu = re.compile('[a-z]')
shuzi = re.compile('[0-9]')
kongbaizifu = re.compile('\s')
hangshu = re.compile('\n')
print('字母个数:',len(zimu.findall(s)))
print('数字个数:',len(shuzi.findall(s)))
print('空白字符个数:',len(kongbaizifu.findall(s)))
print('其他字符:',len(s)-len(zimu.findall(s))-len(shuzi.findall(s))-len(kongbaizifu.findall(s)))
print('行数:',len(hangshu.findall(s)))
print('所有字符个数:',len(s))
duozimudanci = re.compile('\\b[a-z]+\'?[a-z]*-?[a-z]*\'?[a-z]+\\b')
huanhangdanci = re.compile('\\b[a-z]+-\n\n[a-z]+\\b')
danzimudanci = re.compile('\\b[a-z]\\b')
suoyoudanci=[]
suoyoudanci=duozimudanci.findall(s)+huanhangdanci.findall(s)+danzimudanci.findall(s)
print('单词数:',len(suoyoudanci))
c = collections.Counter(zimu.findall(s))
d = len(zimu.findall(s))
o = {}
for i in c:
    o[i]=str(100*c[i]/d)[:4]+'%'
print("字母频率:",o)
g = ['between', 'only', 'his', 've', 'mightn', 'here', 'having', "you've", 'as', 'with', 'did', 'few', 'further', 'herself', 'their', "mustn't", "shouldn't", "she's", 'shan', 'myself', "haven't", 'an', 'your', 'above', 'its', 'has', "won't", 'haven', 'now', 'mustn', 'why', "it's", 'under', "you'd", 'off', 'after', 'own', 're', 'himself', 'but', "mightn't", 'of', 'aren', 'again', 'hadn', "needn't", "wouldn't", 'can', 'weren', "don't", 'will', "you'll", 'there', 'both', 's', 'over', 'up', 'isn', "you're", 'what', 'through', 'they', 'each', 'be', 'are', 'my', 'we', "that'll", 'than', 'most', 'had', 'nor', 'on', 'too', 'before', 'all', 'doesn', 'those', 'these', "isn't", 'do', 'whom', 'where', 'itself', 'am', 'i', 'themselves', 'by', 'such', 't', 'ain', 'needn', 'won', 'wasn', 'because', 'a', 'how', 'it', 'for', 'while', 'our', 'same', 'theirs', 'from', 'ourselves', 'about', 'shouldn', 'when', 'until', 'below', 'them', 'more', 'didn', 'to', 'some', 'were', 'no', "hadn't", 'or', "wasn't", "should've", 'ours', "couldn't", 'this', 'hers', 'into', 'does', 'll', 'couldn', 'once', 'have', 'y', 'not', 'she', 'should', 'm', 'being', 'which', 'doing', 'o', "doesn't", 'so', 'ma', 'me', 'is', 'down', 'who', 'yourselves', 'that', 'very', 'her', 'him', 'the', 'in', 'hasn', 'just', 'he', "didn't", 'during', "shan't", 'd', 'against', 'wouldn', 'don', 'then', 'any', "hasn't", 'at', 'yourself', 'if', 'out', 'and', 'was', 'been', "weren't", 'you', 'yours', "aren't", 'other']
f = collections.Counter(suoyoudanci)
for i in g:
    if i in f.keys():
        del f[i]   
z = sorted(f.items(),key=lambda f:f[1],reverse=True)
print("单词频数排行:",dict(z[:10]))
input()
