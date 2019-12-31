def function(text):
    characters = len(text)      #字符数
    lines = text.count('\n')+(text[-1]!='\n') #行数（通过统计换行符的方式实现，所以要判断最后一行是不是只有换行符）
    text = text.replace('-\n','')    #复原折行单词
    tab1 = str.maketrans(string.ascii_uppercase,string.ascii_lowercase,string.digits)
    text_lowercase = text.translate(tab1)   #把所有字母统一成小写，并删去所有数字
    words1 = text_lowercase.split()   #以空白字符分割字符串，但是得到的列表元素不只有英文单词，还有诸如“**”“Title:”
    words2 = []
    for c in words1:
        c = c.strip(string.punctuation)
        if c != '':
            words2.append(c)              #得到所有删去两端标点符号的英文单词组成的列表words2
    words = len(words2)
    print('莎士比亚全集中共有%d个字符(包含空白字符)，%d行，%d个单词'%(characters,lines,words))     #第一题结束
    print()

    letter_frequency = {}
    for i in text_lowercase:
        letter_frequency[i] = letter_frequency.get(i,0) + 1
    print('莎士比亚全集中各字母(不区分大小写)出现的频率为：')
    for i in string.ascii_lowercase:
        percent = letter_frequency[i]/characters*100
        print('%s\t%.3f%%'%(i,percent))    #第二题结束
    print()

    words_del = ['the','a','an','for','of','and','not','with','on','in','at','to','that','this']  #排除词列表
    words_frequency = {}
    for i in words2:
        if i not in words_del:
            words_frequency[i] =  words_frequency.get(i,0) + 1    #产生字典words_frequency，它的key是单词，value是对应单词出现次数
    a = sorted(words_frequency.items(),key = lambda x:x[1],reverse = True)   #按照value从大到小进行排序
    print("除了the,a,an,for,of,and,not,with,on,in,at,to,that,this以外，莎士比亚全集中出现频率最高的十个单词及他们出现的次数为：")
    for i in range(0,10):
        print('%s\t%d次'%(a[i][0],a[i][1]))   #第三题结束
       
if __name__ == '__main__':
    file = open('bill.txt')
    text =  file.read()
    import string
    function(text)
    file.close
