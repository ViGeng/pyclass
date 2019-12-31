with open ("bill.txt") as bill:
    b = bill.read()
s = len(b)
l = b.count("\n")

import re
b = b.lower()
word = re.findall('\\b[a-z]+\\b',b)
wordh1 = re.findall('\\b[a-zA-Z]+-[a-zA-Z]+\\b',b)
wordh2 = re.findall('[a-zA-Z]+-\n+[a-z]+',b)
wordh3 = re.findall('[a-zA-Z]+\'[a-zA-Z]+',b)
wordn = len(word)+len(wordh1)+len(wordh2)-len(wordh3)

sw = word+wordh1+wordh2
from collections import Counter
frequences = Counter(sw)
time = frequences.most_common(10)
times = frequences.most_common(100)

print("该文件中包含%d个字符，%d行，和%d个单词。" % (s, l, wordn))
print("其中各字母所出现的频率按字母表顺序分别是：")

alpht = list()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    alph = b.count(i)
    alpht.append(alph)
suma = sum(alpht)
for i in range(len(alpht)):
    per = alpht[i]/suma
    percent = "%.2f%%" % (per*100)
    print(alphabet[i],percent)
    
print("此外，其中出现频率最高的单词与其次数分别为：")
print(time)
print("排除虚词后出现频率最高的单词与其次数分别为：")
times2=[]
for i in times:
    if i[0] not in ['do','the', 'and', 'i', 'to', 'of', 'a', 'you', 'my', 'that', 'in', 'is', 'd', 'not', 'for', 'with', 'me', 'it', 's', 'be', 'this', 'your', 'his', 'he', 'but', 'as', 'have', 'thou', 'so', 'him', 'will', 'what', 'by', 'thy', 'all', 'are', 'her','no', 'we', 'shall', 'if', 'on', 'or', 'thee','our', 'o', 'now','from', 'at', 'they',  'she', 'll','here', 'which', 'would', 'more', 'was', 'well', 'then', 'there', 'how', 'am', 'their', 'when','them','an', 'may', 'than', 'one', 'like', 'upon', 'say', 'us', 'make', 'did', 'such', 'were', 'should', 'yet', 'must', 'why', 'see', 'had', 'out', 'tis', 'give', 'where', 'some']:
        times2.append(i)
print(times2)
