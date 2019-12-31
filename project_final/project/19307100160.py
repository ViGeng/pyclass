from collections import Counter
import re

def count_letters(bill):
    f = open(bill,'r')
    s = f.readlines()
    f.close()
    total = 0
    for i in range(97,123):
        count = 0
        for y in s:
            l = re.findall(chr(i),y)
            count += len(l)
        total += count
    freq_l = []
    for i in range(97,123):
        count = 0
        for y in s:
            l = re.findall(chr(i),y)
            count += len(l)
        freq = (count/total)*100 
        freq_l.append(freq)
    alpha_l = [chr(i) for i in range(97,123)]
    af = list(zip(alpha_l,freq_l))
    return af

def count_words(bill):
    f = open(bill,'r')
    text = f.read().lower()
    f.close()
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':
        text = text.replace(ch, "")
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    return items

def count_number(bill):
    f = open(bill,'r')
    text1 = f.read().lower()
    f.close()
    overall_lenth = len(text1)
    text2 = text1.split('\n')
    lines = len(text2)
    word = []
    a = ''
    for line in text2:
        line_list = line.split()
        if line_list != []:
            if line_list[-1][-1] =='-':
                a = line_list[-1][:-1]
                del line_list[-1]
                word += line_list
            else:
                if a == '':
                    word += line_list
                else:
                    line_list[0] = a + line_list[0]
                    a = ''
                    word += line_list
    word_freq = Counter(word)
    words = len(word)
    return overall_lenth,lines,words

def output(overall_lenth,lines,words,items,af):
    print('文本统计如下')
    print('-'*15)
    print('共有%d个字符\n共有%d行\n共有%d个单词'%(overall_lenth,lines,words))
    print('-'*15)
    print('字母出现的频率(百分比)')
    print('{0:<10}{1:>2}'.format('字母', '频率'))
    for i in range(26):
        alphabet,freq = af[i]
        print('{0:<10}{1:>5.2f}%'.format(alphabet,freq))
    print('-'*15)
    print('频率最高的十个单词及次数')
    print('{0:<10}{1:>2}'.format('词', '次数'))
    for i in range(10):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))
    

def main():
    bill = 'bill.txt'
    overall_lenth,lines,words = count_number(bill)
    items = count_words(bill)
    af = count_letters(bill)
    output(overall_lenth,lines,words,items,af)
    

if __name__ == '__main__':
    main()
    
