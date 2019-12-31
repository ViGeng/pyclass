import re

def text_num():
    with open(file,'r') as f:
        all_text = f.read()
        p = 0
        for i in all_text:
            p += 1
        print('字符数(包含空白字符)为：%d' %(p))
        
    with open(file,'r') as f:
        text_list = f.readlines()
        count = 0
        for i in text_list:
            count += 1
        print('行数为：%d'%(count))
        
def get_words():
    with open(file,'r') as f:
        all_text = f.read()
        text = all_text.split(sep='\n')
        text = [i for i in text if i != '']
        i = 0
        l = []
        while True:
            pattern = r'\b[A-Za-z0-9_\'-]+\b'
            l1 = re.findall(pattern,text[i])
            l2 = re.findall(pattern,text[i+1])
            if not text[i].endswith('-'):
                l.extend(l1)
            else:
                l1[-1] = l1[-1].rstrip('-') + l2[0]
                del l2[0]
                l.extend(l1+l2)
            i += 1
            if i == len(text)-1:
                break
        return l

def get_word_nums():
    l = get_words()
    print('单词数为：%d' % (len(l)))

def alpha_times():
    with open(file,'r') as f:
        counters = dict()
        count = 0
        all_text = f.read()
        for i in all_text:
            if i.isalpha():
                count += 1
                i = i.lower()
                counters[i] = counters.get(i,0) + 1
        counters_sorted = sorted(counters, key=lambda x: ord(x))
        for item in counters_sorted:
            print('字母%s(或字母%s)的频率为:%.2f%%' % (item.upper(),item.lower(),(counters[item]/count)*100))

def get_topten():
    counters = {}
    l = get_words()
    for i in l:
        i = i.lower()
        counters[i] = counters.get(i,0) + 1
    counters_sorted = sorted(counters, key=lambda x: counters[x], reverse = True)
    print('文中出现频率最高的10个单词及其次数为')
    for x in counters_sorted[:10]:
            print('%s\t\t出现次数:%d' % (x,counters[x]))

if __name__ == '__main__':
    file = 'bill.txt'
    text_num()
    get_words()
    get_word_nums()
    print('-'*40)
    alpha_times()
    print('-'*40)
    get_topten()
