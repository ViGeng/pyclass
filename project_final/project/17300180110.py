'''notes:
1. 以下认为you're是两个单词
2. 以下认为sea-side e-mail是两个单词
'''

import re
import string

def replace(text):
    #替换所有数字为空格
    tab=str.maketrans('0123456789',' '*10)
    result=text.translate(tab)
    return result


def deal_hyphen(text):
    '''处理同一单词被分成两行的情况,
       方法是去掉句末的'-'将下一行的首个单词拼到本行末尾'''
    text_splitlines=replace(text).splitlines()
    text_splitlines=[item for item in text_splitlines if item]
    for i in range(len(text_splitlines)-1):
        if len(text_splitlines[i])>=2:
            if len(text_splitlines[i+1])>=1:
                if text_splitlines[i][-1]=='-':
                    del_=text_splitlines[i].rstrip('-')
                    a=text_splitlines[i+1].split()
                    new_text_splitlines=''.join((del_,a[0]))
                    text_splitlines[i]=new_text_splitlines
                    del a[0]
                    text_splitlines[i+1]=' '.join(a)
    result=' '.join(text_splitlines)
    return result


def changed_text(text):
    '''将去掉了所有数字，并且处理了同一单词被分成两行问题的文本的所有非字母
       字符换成空格'''
    text1=deal_hyphen(text)
    result=re.sub(r'\W', ' ',text1)
    return result

def count_gbk_lines_words(text):
    '''字符数，行数'''
    gbk=len(text)
    text_bylines=text.splitlines()
    num_lines=len(text_bylines)
    word_list=changed_text(text).split()
    words=len(word_list)
    print('文本的字符数是: %d '% (gbk))
    print('文本的行数是:   %d '% (num_lines))
    print('文本的单词数是：%d ' %(words))
    

def alphabet_frequency(text):
    '''各字母出现的频率'''
    text_unify=text.lower()
    d={}
    for char in text_unify:
        if ord('a')<=ord(str(char))<=ord('z'):
            if char not in d :
                d[char]=1
            else:
                d[char]+=1
    d_values=d.values()
    total_alphabet=sum(d_values)
    for alphabet in d:
        d[alphabet]=d[alphabet]/total_alphabet
    return d


def word_frequency(text):
    '''各单词出现的次数'''
    text_modify=changed_text(text).split()
    word_dict={}
    for word in text_modify:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    return word_dict

def word_frequency_ahead(text,n=10):
    '''删除部分虚词，冠词，连词，代词等，再找出出现最多的10个单词（若有并列
则一起输出）'''
    empty_words=['the','and','a','an','but','to','for','at','on','of'\
                 ,'with','or','in','do','did','of','with','is','was'\
                 ,'are','were','so','as','she','he','they','The','and'\
                 ,'I','you','my','d','t','s','not','me','And','it','that','be'\
                 ,'his','your','this','him','her','will','have','To','That','we'\
                 ,'no','by','shall','all','from','But','our','what','What','am'\
                 ,'would','O','thou','thy','thee','ll','more','them','A','their'\
                 ,'if','For','If','us','You','here','now','My']
    dict1=word_frequency(text)
    for word in empty_words:
        if word in dict1:
            del dict1[word]
    list_dict=list(dict1.items())
    list_dict.sort(key=lambda item:item[1],reverse=True)
    until_number=list_dict[n-1][1]
    ahead=[items for items in list_dict if items[1]>=until_number]
    return ahead


if __name__=='__main__':
    with open('bill.txt','r',encoding='utf-8') as file:
        text=file.read()
    
    count_gbk_lines_words(text)
    frequency_alphabet=alphabet_frequency(text)
    frequency_ahead_words=word_frequency_ahead(text,n=10)
    print('='*40)
    print('字母出现的频率如下:')
    
    for alphabet in range(ord('a'),ord('z')+1):
        if chr(alphabet) in frequency_alphabet:
            print('%s 在文本中出现的频率是 %.5f' % \
                  (chr(alphabet),frequency_alphabet[chr(alphabet)]))
        else:
            print('%s 在文本中出现的频率是 %d' % (chr(alphabet), 0))
    #频率保留到小数点后5位
            
    print('='*40)
    print('出现频率最多的十个词以及次数依次是:')
    for item in frequency_ahead_words:
        print('%s\t 出现的次数是 \t %d' % (item[0],item[1]))


    
    
    
    
    


