def sta_char(filename):
#统计字符数（包括空白字符）
    num = 0
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
        #以上是打开文件，下面是操作代码
        
    else:
        for s in content:
            num += 1
    print("这篇文本共有%d个字符\n" %num)
    


def sta_lines(filename):
#统计行数
    num = 0
    try:
        with open(filename) as f_obj:
            content = f_obj.readlines()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
        #以上是打开文件，下面是操作代码
        
    else:
        for line in content:
            num += 1
    print("这篇文本共有%d行\n" %num)
    

    
def sta_words(filename):
#统计单词数（考虑到行尾折行）
    num = 0
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
        #以上是打开文件，下面是操作代码
        
    else:
        num_1 = content.split()
        print('这篇文本共有%d个单词\n' %len(num_1))
      


def letter_fre(filename):
#统计字母出现频率（不区分大小写）
    num = 0
    d = {}
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
        #以上是打开文件，下面是操作代码
        
    else:
        content = content.lower()
        for s in content:
            if s.isalpha():
                num += 1
                d[s] = (d[s]+1) if s in d else 1
        print('这篇文本共有%d个字母\n' %num)
        for s in d:
            print('字母%s出现的频率是%.4f%%' %(s,d[s]/num*100))
        print('\n')

   

def most_fre(filename):
#统计最高频率的10个单词及出现次数
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
        #以上是打开文件，下面是操作代码
        
    else:
        d = {}
        content = content.lower()
        content = content.split()
        #将字母转为小写
        for word in content:
            d[word] = (d[word]+1) if word in d else 1
        d = sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
        #统计次数并排序
        print('出现频率前10的单词和出现的次数如下:\n')
        for i in range(0,10):
            print(d[i])
        print('\n')
        


def most_fre_plus(filename):
#创建排除词列表以后统计10个频率最高单词及次数
    fre_dict = ['the','i','you','and','to','of','a','in','this','that','for','with',
                'be','are','my','is','not','your','his','as','but','he','it','have',
                'thou','me','will','by','so','thy','what','if','shall','do','all','we',
                'him','or','our','her','no','on','from','at','they','would','which','was',
                'their','am']
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist."
        print(msg)
        #以上是打开文件，下面是操作代码

    else:
        d = {}
        content = content.lower()
        content = content.split()
        #将字母转为小写
        for word in content:
            if word not in fre_dict:
                d[word] = (d[word]+1) if word in d else 1
        d = sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
        #统计次数并排序
        print('剔除高频词后，出现频率前10的单词和出现的次数如下:\n')
        for i in range(0,10):
            print(d[i])

    
    
if __name__ == '__main__':
    filename = 'bill.txt'
    sta_char(filename)
    sta_lines(filename)
    sta_words(filename)
    letter_fre(filename)
    most_fre(filename)
    most_fre_plus(filename)




