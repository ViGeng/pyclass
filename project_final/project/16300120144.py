import re
import string

def count_text():
    f=open('bill.txt', 'r', encoding='ASCII')
    text = f.read()
    strings = re.findall(r'.|\n',text)
    letters = re.findall('[a-zA-Z]',text)
    p_word = r'\b[a-zA-Z]+[-\']?[a-zA-Z]*\b'
    p_endline = r'\b[a-zA-Z]+-\n'
    words= re.findall(p_word,text)
    words_endlines = re.findall(p_endline,text)
    
    f.seek(0)
    lines = f.readlines()
    str_num = len(strings)
    line_num = len(lines)
    word_num = len(words)-len(words_endlines)
    letter_num = len(letters)
    f.close()

    print('文本中的字符数为:%d'%str_num)
    print('文本中的行数为:%d'%line_num)
    print('文本中的单词数为:%d'%word_num)
    print('-'*75,'\n')
    
    for i in string.ascii_lowercase:
        items = re.findall(i,text,re.I)
        item_num = len(items)
        percent = item_num / letter_num * 100
        print('字母%s出现的百分比是%.3f%%'%(i,percent))
        
    print('-'*75,'\n')

    word_dict = dict()
    exclude_list = ['a','an','the','not','in','at','on','to','with','of','for','and','or','but','oh','ah','alas']
    print('以下虚词不计入统计:',*exclude_list,'\n',sep=' ')
    
    for i in words:
        check_i = i.lower()
        if check_i not in exclude_list:
                word_dict[check_i] = word_dict.get(check_i,0) +1
            
          
    word_list = sorted(word_dict.items(),key=lambda i: i[1],reverse=True) #sorted返回一个列表！[('kitty', 326), ('lauren', 44), ('bob', 1)]  
    top_10 = word_list[:10]
    
    n = 1
    for i in top_10:
        print('出现频率第%d位的词是%s,出现次数为:%d次'%(n,i[0],i[1]))
        n+=1


if __name__ == '__main__':
    count_text()
    




    
    
        
        

    






