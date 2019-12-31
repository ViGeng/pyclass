import re
with open('bill.txt', 'r') as fr:
    word_dict = {} # 用于统计 word：个数
    word_list = [] # 用于存放所有单词

    for line in fr.readlines():
        for word in line.strip().split(" "):
            word_list.append(re.sub(r"[^a-z]+", "", word.lower()))
    word_sets = list(set(word_list))   # 确保唯一
    word_dict = {word: word_list.count(word) for word in word_sets if word}

fr=open('bill.txt','r', encoding='UTF-8')
content=fr.readlines()
contentLines=''
characers=[]#存放不同字的总数
rate={}#存放每个字出现的频率
 
# 依次迭代所有行
for line in content:
    line=line.strip()
    #如果是空行，则跳过
    if len(line)==0:
        continue
    contentLines = contentLines + line
    # 统计每一字出现的个数
    for x in range(0,len(line)):
        # 如果字符第一次出现 加入到字符数组中
        if not line[x] in characers:
            characers.append(line[x])
        # 如果是字符第一次出现 加入到字典中
        if line[x] not in rate:
            rate[line[x]]=1
        #出现次数加一
        rate[line[x]]+=1
lines = len(content)

# 对字典进行倒数排序 从高到低 其中e表示dict.items()中的一个元素，
# e[1]则表示按值排序如果把e[1]改成e[0]，那么则是按键排序，
# reverse=False可以省略，默认为升序排列

rate=sorted(rate.items(), key=lambda e:e[1], reverse=True)
 
print('全文共有%d个字符'%len(contentLines))
print('-' * 30)
print()

print('全文共有%d行'%lines)
print('-' * 30)
print()

print('一共有%d个不同的单词'%len(word_dict))
print('-' * 30)
print()


def main():
    infile = open('bill.txt',"r")
    counts = 26 * [0]
    for line in infile:
        countLetters(line.lower(),counts)
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + ":出现了:" + str(counts[i]) + (" 次" if counts[i] == 1 else " 次"),
                  '     出现的频率为:{:.2f}'.format((counts[i]/4880025)*100)+'%')
    infile.close()
    
def countLetters(line,counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1 #利用ascII值得偏移得到索引

if __name__ == "__main__":
    main()


delist = ['is','as','i','my','and','but','or','in','on','at','for','a' ,'an','the','ah','oh','to','of','that','not','this',
         'with','me','be','his','he','the','so','him','by','what','they','all','are','her','it','have','we','our','if',
          'will','it','you','your']

for i in delist:
    if i in word_dict:
        word_dict.pop(i)
result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:10]
print('本文中出现最多的单词及其个数为：')
print(result)
