file = open('bill.txt')
text = file.read()
import re

print('在莎士比亚全集中')


#字符
ch = re.findall(r'\d|\D',text)
print("包含",len(ch),"字符")

#字母频率
print('各个字母出现次数和频率如下')
letters = re.findall(r'[a-zA-Z]',text)
b = len(letters)

letters_list = []
for x in range(len(letters)):
	letters_list.append(letters[x][0].lower())

letters_set = sorted(set(letters_list))
for i in range(len(letters_set)):
	letter = letters_set[i]
	a = letters_list.count(letter)
	print('%-5s %-3s %10.3f' % (letter,a,a/b))

#行数

with open('bill.txt','r') as file:
        count = 0
        for i in file:
                if len(i.strip()) == 0:
                        count = count
                else:
                        count += 1
        print("共有",count,"行")



#单词
word_dict = {} 
word_list = []
c = text.strip('- \n')
word_list = c.replace(',',' ').split()
print("单词数量为",len(word_list))

word_sets = list(set(word_list))   
word_dict = {word: word_list.count(word) for word in word_sets if word}
ignore_list=['the','of','for','a','and','that','this','to','in','on','with','you','I','me','it','his','your','is','are']
for key in ignore_list:
    if key in word_dict.keys():
        del word_dict[key]
result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:10]
print(result)





