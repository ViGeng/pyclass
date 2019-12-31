def sort_by_value(item):
    return item[1]

def main():
    filename = 'bill.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    linenum = len(lines)
    strnum = 0
    for i in lines:
        strnum = strnum + len(i)
    #把换行单词连起来
    article1 = ''.join(lines)
    article2 = article1.replace('-\n\n','')
    article = list(article2)
    #去掉非字母符号
    import string
    n = 0
    while n < len(article):
        if article[n] not in string.ascii_letters:
            if article[n] != ' ':
                article[n] = ''
        n += 1
    article3 = ''.join(article)
    #可能连续存在多个空格，按照空格给单词计数
    import re
    article3 = article3.strip()
    article4 = re.split('[\s]+', article3)
    wordnum = len(article4)
        
    print('文本包含%d行'% (linenum))
    print('文本包含%d个字符'% (strnum))
    print('文本包含%d个单词'% (wordnum))
    print()

    #将字母都转换为小写，计算各字母出现次数
    article5 = ''.join(article4)
    lower = article5.lower()
    for i in string.ascii_lowercase:
        a = lower.count(i) / len(lower)
        b = 100 * a
        print('字母%s出现的频率是%.5f%%'% (i, b))
    print()

    #将article4中字母都转化为小写
    m = 0
    while m < len(article4):
        article4[m] = article4[m].lower()
        m += 1
    #这里article4是一个由文本单词组成、全部是小写字母、有重复的单词列表
    words = list(set(article4))
    #words是一个不重复的出现过的单词的列表
    #要剔除掉哪些单词，以空格分开
    delete = input('剔除这些单词，两个单词之间用空格隔开，如果无需剔除则按回车键')
    delete1 = delete.split(' ')

    #创建一个{单词：次数}的列表
    word_num = dict()
    for word in article4:
        if word in word_num:
            word_num[word] += 1
        elif word not in word_num:
            word_num[word] = 1
    #删掉剔除的单词
    for word in delete1:
        if word in word_num:
            del word_num[word]
    #进行按出现次数的排序
    order = sorted(word_num.items(), key = sort_by_value, reverse = True)
    #输出除了排除词之外出现前十多的单词
    print('除了排除词之外：')
    p = 0
    while p < 10:
        print('出现第{}多的单词是{}，一共出现了{}次'.format(p+1, order[p][0], order[p][1]))
        p += 1
        

if __name__ == '__main__':
    main()
