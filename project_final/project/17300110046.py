import re
from collections import Counter

#统计字符 行数 单词
def question1():
    file1=open('bill.txt','r',encoding='utf-8')
    print('第一题')
    a=file1.read()
    a.lower()
    count=len(a)
    print('字符数：',count,end=' ')
    lines=len(a.split('\n'))
    print('行数：',lines,end=' ')
    word='[a-z]+'
    wordlist=re.findall(word,a)
    print('单词数：',len(wordlist))
    file1.close()

#统计字频
def question2():
    file2=open('bill.txt','r',encoding='utf-8')
    print('第二题')
    a=file2.read()
    a.lower()
    re=Counter(a)
    count={}
    sum1=0
    i=97
    while i<=122:
        a=chr(i)
        sum1+=re[a]
        i+=1
    i=97
    while i<=122:
        a=chr(i)
        count[a]=(re[a]/sum1*100)
        i+=1
    print('各字母出现频率：')
    for key, value in count.items():
        print(key + ": " + str(value))
    file2.close()

def main():
    question1()
    question2()
if __name__=='__main__':
    main()
    
# 统计词频

filename1 = 'bill.txt'
E = str(list(open(filename1, encoding = 'utf-8'))).lower()


def del_pun(f_name):
    """去掉文本中标点"""
    import re
    a = f_name.split()
    return list(a)


def cal_fre(f_name):
	"""统计文本中各字字频"""
	d = {}
	for i in f_name:
		if i.lower() not in d.keys():
			d[i] = 1
		else:
			d[i] += 1
	return d


def show_seq(fre, num):
	"""显示字典fre中字频前num的排序"""
	seq = sorted(fre.items(), key=lambda x: x[1], reverse=True)
	for key, value in seq[:num]:
		print(key + ": " + str(value))


e = del_pun(E) # 去标点
e_fre = cal_fre(e) # 字频

print("第三题 词频前10： ")
show_seq(e_fre, 10)
