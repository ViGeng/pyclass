#
line_count = 0
word_count = 0
character_count = 0
f=open ('bill.txt','r',encoding='utf-8')
for line in f:
    if line.strip() == '':
         continue
    word=line.split()
    line_count+=1
    word_count+=len(word)
    character_count+=len(line)
print('{0}文件有{1}个单词'.format('bill.txt',word_count))
print('{0}文件有{1}行'.format('bill.txt',line_count))
print('{0}文件有{1}个字符'.format('bill.txt',character_count))


#
import string
with open('bill.txt','r')as f:
    words = f.read()
xiaoxie=string.ascii_lowercase
daxie=string.ascii_uppercase
t=''
u=''
for x in words:
    if x in xiaoxie:
        t=t+x

for y in words:
    if y in daxie:
        u=u+y

t=t+u
w=t.lower()
a=len(w)
for i in xiaoxie:
    b=w.count(i)
    c=b/a
    d=round(c,4)
    e='%.2f%%'%(d*100)
    print('字母{}的频率是{}'.format(i,e))



#
keep = {"a", "b", "c", "d", "e", "f", "g", "h", "i",
          "j", "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z", " ", "-", "\'"}


def Low(s):

    result = ''

    for i in s.lower():

        if i in keep:

            result += i

    return result
def Num(s):
    s = Low(s)
    words = s.split()
    
    dict = {}
    for i in words:
        if i in dict:
            dict[i] +=1
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

with open('bill.txt','r',encoding='utf-8') as f:
 text=f.read()
 text=text.lower()
 d = order(text)
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

          print ('频率第%s 次数为%s 单词为%s' %(i, count, word))

          i += 1
   





