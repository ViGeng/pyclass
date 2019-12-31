import re
import string
def basic_stats():
    global words
    print("基础性统计如下:")
    print("%-8s%-8d"%("总字符:",len(text)))
    print("%-8s%-8d"%("总行数:",len(text.split('\n'))))
    words=re.findall(r"\b[a-z']+\b",text.replace("-\n","").lower())
    print("%-8s%-8d"%("总单词数:",len(words)))
def letter_frequency():
    count=dict()
    print("\n各字母出现的频率如下:\n{0:^6s}{1:^20s}".format("letter","frequency"))
    for letter in text.lower():
        if letter in string.ascii_lowercase:
            count[letter]=count.get(letter,0)+1
    total_num=sum(count.values())
    for letter in string.ascii_lowercase:
        print("{0:^6s}{1:^20.4%}".format(letter,count[letter]/total_num))
def word_frequency(remove_list=list(),stats=list()):
    stat=dict()
    if remove_list:
        input_words="虽然你并没有输入什么" if remove_list==[""] else ' '.join(remove_list)
        print("\n除输入单词(%s)外，出现频率最高的十个单词及其出现的次数为:"%input_words)
    else:
        print("\n文中出现频率最高的十个单词及其出现的次数为:")
    print("{0:^6s}{1:^8s}{2:^8s}".format("rank","word","times"))
    if not stats:
        for word in words:
            stat[word]=stat.get(word,0)+1
        stats=sorted(stat.items(),key=lambda x:x[1],reverse=True)
    count=0
    for pair in stats:
        if pair[0] not in remove_list:
            print("{0:^6d}{1:^8s}{2:^8d}".format(count+1,pair[0],pair[1]))
            count+=1
        if count>=10:
            break
    return stats
def main():
    global text
    while True:
        try:
            document=input("请输入需要统计文件的路径(如:bill.txt):")
            with open(document,'r') as f:
                text=f.read()
            break
        except:
            print("请输入正确的文件路径!")
    remove_list=input("请输入需要排除的单词，以空格分割:").split(" ")
    basic_stats()
    letter_frequency()
    stats=word_frequency()
    word_frequency(remove_list,stats)
if __name__=="__main__":
    main()
