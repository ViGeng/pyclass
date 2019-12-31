import re
#统计每行每个字母的个数
def processLine(line, CharacterCounts):
    letter=0
    for character in line:
        if ord(character) in range(97, 123):
            CharacterCounts[character] += 1
            letter+=1
    return letter

#构建字母字典
def createCharacterCounts(CharacterCounts):
    for i in range(97, 123):
        CharacterCounts[chr(i)] = 0

#统计文本行数、字符数、单词数
def read_file_info(filename):
    line_count=0
    word_count=0
    character_count=0
    with open(filename, 'r+', encoding='UTF-8') as f:
        for line in f:
            word=line.split()
            line_count+=1
            word_count+=len(word)
            if(line[len(line)-1]=='-'):#判断行尾是否有拆分单词，如果有的话下行再+1
                word_count-=1
            character_count+=len(line)
    print('本文档字符数共计：',character_count,'行数：',line_count,'单词数：',word_count)
    f.close()

#统计文本字母频率
def count_letters(filename):
   CharacterCounts = {}
   #字母总数
   sum_letter=0
   createCharacterCounts(CharacterCounts)
   with open(filename, 'r+', encoding='UTF-8') as f:
       for line in f:
           sum_letter+=processLine(line, CharacterCounts)
   #从字典中获取数据对
   pairs = list(CharacterCounts.items())
   #列表中的数据对交换位置,数据对排序
   items = [[x,y] for (y,x) in pairs] 
   items.sort(reverse=True)
   #输出count个数词频结果
   print("文档字母总数为：",sum_letter,"，各字母频率如下(百分比保留2位小数)，频率从高到底依次为：")
   for i in range(len(items)):
       print(items[i][1]+"\t",round(int(items[i][0])/sum_letter*100,2),"%")
   f.close()

def findWords(filename):
    d = {}
    stopwords = {'the','a','on','an','to','it','of','in','d','is','s','and','with','i','for','be','this',''} 
    with open(filename,encoding='utf8')as f:
        for line in f:
            #\W正则表达式匹配所有单词
            words = re.split(r"\W|_",line)
            for word in filter(lambda word :word.lower() not in stopwords,words):
                #统计
                d[word]= d.get(word,0)+1
    print("本文档除停用词外词频最高的十个词如下：")
    most_top10 = sorted(d.items(),key = lambda x :x[1],reverse = True )[:10]
    for item in most_top10:
        print(item)
    f.close()

if __name__ == '__main__':
    read_file_info("./bill.txt")
    count_letters("./bill.txt")
    findWords("./bill.txt")