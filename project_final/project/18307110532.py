def alpha_counter(x):
    x=x.lower()
    num=[]
    dic={}
    for i in x:
        if not i.isalpha():
            num.append(i)
        else:
            if i in dic:
                continue
            else:
                dic[i]=x.count(i)
    all_letters=0
    for k,v in dic.items():
        all_letters+=v
    for k,v in dic.items():
        dic[k]='{:.2%}'.format(v/all_letters)
   
    return dic

def delete_words(x):
    result=''
    for w in x.lower():
        if w not in keep:
            result+=w
    return result

def make_freq(x):
    x=delete_words(x)
    words=x.split()
    dic={}
    for w in words:
        if w in dic:
            dic[w]+=1
        else:
            dic[w]=1
    return dic

def words_order(x):
    d=make_freq(x)
    d=sorted(d.items(),key=lambda item:item[1],reverse=True)
    return d
    


keep={",",".","'","}","!"}

file_name='bill.txt'
with open(file_name) as file_obj:
    contents=file_obj.read()
    lines=contents.split('\n')
    all_words=contents.split(' ')
    word=contents.count('-\n')
        
num_string=len(contents)
num_lines=len(lines)
num_words=int(len(all_words))-word



print('文本文件包含',num_string,'个字符。')
print('文本文件包含',num_lines,'行。')
print('文本文件包含',num_words,'个单词。')

print('各字母出现的频率为：')
a=alpha_counter(contents)
for k,v in a.items():
    print(k,v)

print('文件中出现频率最高的10个单词及它们出现的次数如下：（稍等几秒）')
a=words_order(contents)
for word,count in a[:10]:
    print(word,count)

file_obj.close()
