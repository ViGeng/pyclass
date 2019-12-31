##要求计算并打印有关文本文件内容的统计数据。包括：
##1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（
##注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。
##2。文件中各字母（不区分大小写）出现的频率（所占百分比）。
##3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，
##你也可以创建一个排除词的列表，其中包含要忽略的所有单词，
##然后统计这张表以外出现频率最高的10个单词以及其出现的次数
import re

def main():
    q=[]
    while True:
        w=input("请输入需排除的单词：")
        q.append(w)
        if w=="":
            break
    letters='abcdefghijklmnopqrstuvwxyz'
    text=open("bill.txt").read()
    a=len(text)
    lines=text.splitlines()
    b=len(lines)
    words=re.split(r'\W+',text.lower())
    c=len(words)
    d=0
    z=0
    g=0
    letter_fre=dict()
    word_fre=dict()
    for letter in text.lower():
        if letter in letters:
            #if letter in letter_fre:
                #letter_fre[letter]=letter_fre[letter]+1
            #else:
                #letter_fre[letter]=1
            d+=1
            letter_fre[letter]=letter_fre.get(letter,0)+1
    for word in words:
            word_fre[word]=word_fre.get(word,0)+1
    words_fre=sorted(word_fre.items(),key=lambda t:-t[1])
    print("共有字符数:",a)
    print("共有行数:",b)
    print("单词数:",c)
    print("文件中各字母（不区分大小写）出现的频率（所占百分比)")
    print()
    print("%5s%8s"%("字母","百分比"))
    for i in letters:
        print("%5s%10.2f%%"%(i, letter_fre[i]/d*100))
    print()
    print("文件中出现频率最高的10个单词及它们出现的次数")
    print()
    print("%5s%8s"%("单词","次数"))
    while z<=9:
        if words_fre[g][0] not in q:
            print("%6s%10d"%(words_fre[g][0],words_fre[g][1]))
            z+=1
        g+=1

if __name__=="__main__":
    main()
