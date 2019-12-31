# -*- coding: utf-8 -*-

def f1():
    line_count=0
    word_count=0
    character_count=0
    with open('bill.txt','r',encoding='utf-8') as f:
        for l in f:
            line=l.strip('\n')
            word=line.split()
            if word!=[]:
                line_count+=1
                if word[-1][-1]=='-':
                    word_count+=len(word)-1
                else:
                    word_count+=len(word)
            character_count+=len(line)
    print('行数：',line_count)
    print('单词数：',word_count)
    print('字符数：',character_count)

def f2():
    characers = []  # 存放不同字的总数
    rate = {}  # 存放每个字出现的频率
    all_num = 0
    with open('bill.txt', 'r', encoding='utf-8') as f:
        # 依次迭代所有行
        for line in f:
            # 去除空格
            line = line.strip()
            # 如果是空行，则跳过
            if len(line) == 0:
                continue
            # 统计每一字出现的个数
            for x in range(0, len(line)):
                l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                if line[x].lower() in l:
                    # 如果是字符第一次出现 加入到字典中
                    if line[x].lower() not in rate:
                        rate[line[x].lower()] = 1
                    # 出现次数加一
                    rate[line[x].lower()] += 1
                    all_num+=1
        rate = sorted(rate.items(), key=lambda e: e[1], reverse=True)
        for i in rate:
            if i[0]!=' ':
                bfb = ('%.4f' % ((int(i[1])/all_num)*100))
                print("(", i[0], ") 出现 ", i[1], "次  所占百分比 ", str(bfb)+'%')

def f3():
    def getText():
        txt = open("bill.TXT", "r", encoding='UTF-8').read()  # 打开文件
        txt = txt.lower()  # 全部转成小写
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
        return txt

    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    stopwords = ['the', 'd','s', 'i', 'and', 'to', 'of', 'a', 'you',
                 'my', 'in','is', 'that', 'not', 'me', 'with', 'it', 'be', 'his', 'your', 'for', 'this', 'he', 'she', 'him', 'her',
                 'and', 'have', 'will','as', 'so', 'but', 'all', 'to', 'are', 'do', 'what','we','if','or','our']
    for word in words:
        if word not in stopwords:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 排序
    for i in range(10):
        word, count = items[i]
        print('词：{}，出现次数：{}'.format(word, count))

if __name__ == '__main__':
    f1()
    f2()
    f3()