'''要求计算并打印有关文本文件内容的统计数据。包括：
1。用户指定的文本文件中，包含多少字符（也包括那些空白字符）、多少行、多少单词（注意行尾单词折行的问题，这种情况通常行尾会有连字号-）。
2。文件中各字母（不区分大小写）出现的频率（所占百分比）。
3。文件中出现频率最高的10个单词及它们出现的次数。通常出现频率最高的是一些the这样的虚词，你也可以创建一个排除词的列表，其中包含要忽略的所有单词，然后统计这张表以外出现频率最高的10个单词以及其出现的次数
'''
import collections
import string

#question 1
line_count = 0
word_count = 0
character_count = 0


f= open('bill.txt','r',encoding='utf-8')
for line in f:
    if line.strip() == '':
        continue
    word=line.split()
    line_count+=1
    word_count+=len(word)
    character_count+=len(line)
f.close()
f= open('bill.txt','r',encoding='utf-8')
word_list=f.read()

deviation=word_list.count('-')

print('{0}文件有{1}个单词'.format('bill.txt',word_count+deviation))
print('{0}文件有{1}行'.format('bill.txt',line_count))
print('{0}文件有{1}个字符'.format('bill.txt',character_count+deviation*2))



#question 2
deviation=word_list.count('-')
lower_list=word_list.lower()

total_letter=0

for i in string.ascii_lowercase:
    a=lower_list.count(i)
    total_letter+=a
    

for i in string.ascii_lowercase:
    a=lower_list.count(i)
    ratio=a/total_letter
    
    print('字母{}的频率是{:.3f}'.format(i,ratio))


#question 3


keep = {"a", "b", "c", "d", "e", "f", "g", "h", "i",
          "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z", " ", "-", "\'"}


def count(s):
    result = ''
    for i in s.lower():
        if i in keep:
            result += i
    return result

def Num(s):
    s = count(s)
    words = s.split()
    dict = {}
    for i in words:
        if i in dict:
            dict[i] += 1
        else:
                dict[i] = 1
    return dict

def order(s):
    d = Num(s)
    lst = []
    for i in d:
        tuple_dict = (d[i], i)
        lst.append(tuple_dict)
    lst.sort()
    lst.reverse()
    return lst


d = order(lower_list)
i = 1
for count, word in d[:10]:
       if word in {'between', 'only', 'his', 've', 'mightn', 'here', 'having',
               "you've", 'as', 'with', 'did', 'few', 'further', 'herself',
               'their', "mustn't", "shouldn't", "she's", 'shan', 'myself',
               "haven't", 'an', 'your', 'above', 'its', 'has', "won't",
               'haven', 'now', 'mustn', 'why', "it's", 'under', "you'd",
               'off', 'after', 'own', 're', 'himself', 'but', "mightn't",
               'of', 'aren', 'again', 'hadn', "needn't", "wouldn't", 'can',
               'weren', "don't", 'will', "you'll", 'there', 'both', 's',
               'over', 'up', 'isn', "you're", 'what', 'through', 'they',
               'each', 'be', 'are', 'my', 'we', "that'll", 'than', 'most',
               'had', 'nor', 'on', 'too', 'before', 'all', 'doesn', 'those',
               'these', "isn't", 'do', 'whom', 'where', 'itself', 'am', 'i',
               'themselves', 'by', 'such', 't', 'ain', 'needn', 'won',
               'wasn', 'because', 'a', 'how', 'it', 'for', 'while', 'our',
               'same', 'theirs', 'from', 'ourselves', 'about', 'shouldn',
               'when', 'until', 'below', 'them', 'more', 'didn', 'to',
               'some', 'were', 'no', "hadn't", 'or', "wasn't", "should've",
               'ours', "couldn't", 'this', 'hers', 'into', 'does', 'll',
               'couldn', 'once', 'have', 'y', 'not', 'she', 'should', 'm',
               'being', 'which', 'doing', 'o', "doesn't", 'so', 'ma', 'me',
               'is', 'down', 'who', 'yourselves', 'that', 'very', 'her',
               'him', 'the', 'in', 'hasn', 'just', 'he', "didn't", 'during',
               "shan't", 'd', 'against', 'wouldn', 'don', 'then', 'any',
               "hasn't", 'at', 'yourself', 'if', 'out', 'and', 'was',
               'been', "weren't", 'you', 'yours', "aren't", 'other'}:

          print (i, count, word)
          i += 1
   



