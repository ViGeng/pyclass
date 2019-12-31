with open('bill.txt', 'r') as a_file:
    text = a_file.read()
print('共有' + str(len(text)) + '个字符')

with open('bill.txt', 'r') as b_file:
    lines = b_file.readlines()
print('共有' + str(len(lines)) + '行')

for ch in '-':
    text = text.replace(ch, '')
words = len(text.split())
print('共有' + str(words) + '个单词')


text = text.lower()
import re
punctuation = '~`%}$#@&|/_*<>"():!?;\'.,\n 1234567890\[\]'
a_text = re.sub(r'[{}]+'.format(punctuation),'',text)

adict = {}
for e in a_text:
    if e in adict:
        adict[e] += 1
    else:
        adict[e] = 1
total = sum(adict.values())
print('各字母出现的频率为：')
letters = 'qwertyuioplkjhgfdsazxcvbnm'
for i in letters:
    x = adict[i] / total * 100
    print(i,'%.3f' % x + '%')


bdict = {}
functionwords = ('the', 'and', 'of', 'to', 'in', 'that', 'for', 'a ', 'not', 'with', 'be', 'but', 'as')
for word in functionwords:
    text = re.sub(word, '', text)
for t in text.split():
    if t in bdict:
        bdict[t] += 1
    else:
        bdict[t] = 1
s2 = sorted(bdict.items(), key=lambda x:x[1])
print('出现频率最高的10个单词是：')
m = -1
while m >= -10:
    print(*s2[m])
    m -= 1
