import re
import sys

worddict={}
letterdict={}
pattern = r'\b\w+\b'   ##用正则表达式的模式表示所有单词
exceptedwords = ['THE','A','TO','I','AND',
                 'OF','YOU','ME','MY','IN',
                 'THIS','THAT','WE','HE',
                 'NOT','IS','OR','WITH','IT',
                 'YOUR','HIS','BE','IF','ON',
                 'BUT','AS','HAVE','AT','SO',
                 'HIM','WHAT','BY','AN','FOR',
                 'ARE','HER','NO','DO','ALL']    ##去除一些常见词
lower_letters = [chr(i) for i in range(97,123)]
upper_letters = [chr(i) for i in range(65,91)]
allletters = lower_letters + upper_letters
    
def detect_encoding(text):
    encodings = 'ASCII', 'UTF-8', 'GBK'

    for encoding in encodings:
        try:
            with open(text, encoding=encoding) as f:
                f.read(100)
            break
        except UnicodeDecodeError:
            pass
    return encoding


def count_words(filetext):
    wordlist = re.findall(pattern,filetext) 
    for word in wordlist : 
        if word.upper() not in worddict:
            worddict[word.upper()] =1
        else:
            worddict[word.upper()] +=1
    print('文件总共有%s个单词（计重数）'%len(wordlist))
    print(' ')
    countmount = sorted(worddict.items(),key=lambda item:item[1])

    i = 0
    j = 0
    print('文本中出现频率最高（去除单个字母和一些常见词）的十个单词及其出现次数是:')
    while i in range(10):
        if ((countmount[-j-1][0]) not in exceptedwords) and (len((countmount[-j-1][0]))>1) :
            print('%15s  %-10s'%(countmount[-j-1][0],countmount[-j-1][1]))
            j += 1
            i += 1
        else:
            j += 1


def count_letters(filetext):
    for i in filetext:
        if i in allletters: 
            if i.upper() not in letterdict:
                letterdict[i.upper()] = 1
            else:
                letterdict[i.upper()] += 1
        else:
            pass

    total = 0
    for j in letterdict.values():
        total+=j
        
    print('各字母出现的频率是：')   
    for i,j in sorted(letterdict.items(),key = lambda item:item[0]):
        print('%15s  %.2f'%(i,j/total*100))




if __name__ == '__main__':
    filename = input('请输入要统计的文件全名：\n')
    exist = 1
    
    while exist == 1:
        try:
            file = open(filename,'r',encoding = detect_encoding(filename))
            lines = file.readlines()
            exist = 0
        except Exception as e:
            print('您输入的文件名有误,错误如下：')
            print(e)
            exitoption = input('是否还要继续？——Y/N \n')
            option = 1 
            while option == 1:
                if exitoption.upper() in 'YN':
                    option = 0
                    if exitoption.upper()=='N':
                        sys.exit()
                    else:
                        filename = input('请重新输入要统计的文件全名：\n')
                else:
                    exitoption = input('您输入的不是合法字符Y或N，是否还要继续？——(请输入Y或N) \n')


    linenumber = 0
    totalnumber = 0
    filetext= ''
    for line in lines: 
        if (line.strip()).endswith('-'):
            filetext+=(line.strip('\n').strip('-')) # excepting those lines ended with '-'
        else:
            filetext+=(line.replace('\n',' ',1))
        linenumber += 1
        totalnumber += len(line)

    print(' ')
    print('文件总共有%s行'% linenumber)
    print('文件总共有%s字符'% totalnumber)
    
    count_words(filetext)
    print(' ')
    count_letters(filetext)
    
    file.close()

