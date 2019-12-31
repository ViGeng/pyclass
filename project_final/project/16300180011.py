
import string
import time

def testtrue(x):
    ##校验调试用
    if x:
        print('It\'s true')
    else:
        print('Wrong!')


def listgene(textname='bill.txt'):
    ##输出字符数、行数和单词数
    ##生成一个一个仅textname中小写字母串ascstr = 'theglobal...licence'
    ##生成一个存放单词的列表wordslist = ['the' ... 'lience']
    ##所有生成内容首尾无空格,且皆为小写
    
    f = open(textname,'r')
    alist = f.readlines()
    f.close()

    numstr = 0 #包括所有空格类字符数
    numrow = 0 #所有行数(不包括空行)
    Alist = [] #将alist中空白行去除
    for i in alist:
        numstr += len(i)
        if  i.strip(string.whitespace):
            numrow +=1
            Alist.append(i)
            
    s1 = ''.join(Alist)
    s1 = s1.replace('-\n','') #若默认以'-\n'为结尾的都是折行
    s2 = alist[0]             #要求折行必须满足折行前一个字母,换行后第一个是小写字母
    numlist = range(len(Alist) - 1) #循环从一一直到倒数第二行
    for i in numlist:
        try:
            if Alist[i][-2:]=='-\n' and Alist[i][-3].isalpha() and Alist[i+1][0].islower():

                s2 = s2[0:-2] + Alist[i+1]
            else:
                s2 = s2 + Alist[i+1]
        except:
            s2 = s2 + Alist[i+1]
    xstr = string.digits + string.punctuation + string.whitespace
    s2 = s2.strip(xstr)
    ##保证s2以字母开头结尾
    ##  testtrue(s1==s2) 发现两者不同，找到'''Lie there what hidden woman's fear there will-\n  We'll have a swashing and a martial outside'''不一定是折行
    ##  这里我们采取s2
    ##  s2是长字符串且由非字母分隔的字符串即为单词


    temlist = []   #临时存放所有
    asctemlist =[] #临时存放仅字母
    for i in s2:
        if i in string.ascii_letters:
            temlist.append(i)
            asctemlist.append(i)
        else:
            if temlist[-1]==' ':
                pass
            else:
                temlist.append(' ')


    global ascstr
    longstr = ''.join(temlist)
    ascstr  = ''.join(asctemlist)
    longstr = longstr.lower()
    ascstr  = ascstr.lower()
    
    

    ##  确保longstr和ascstr首尾无空格
    ##  longstr词间仅单个空格
    ##  优化单词情况,去除网址中(www,org,http)和b-z的大小写
    ##  注意到形如I'm,I'd等算作一个单词(算法中分成)故此算法可行


    xlist = ['www','org','http'] + list(string.ascii_letters)
    xlist.remove('a')
    xlist.remove('A')
    xlist.remove('I')
    
##  wordslist1 = longstr.split()
##  for i in wordslist1:                 算法太差耗时太久(考虑到有序列表移动慢)
##      if i in xlist:                   改从字符串着手
##          wordslist1.remove(i)

    global wordslist
    wordslist = []
    end = -1
    strtem = longstr + ' '
    for i in range(len(strtem)):
        if strtem[i] ==' ':
            if strtem[end+1:i] in xlist:
                pass
            else:
                wordslist.append(strtem[end+1:i])
            end = i
        
    print('{0:^38}'.format('统计部分1'))
    print('+' + '-'*38 + '+')
    print('|字符数为:%29d|'%numstr)
    print('|行数为(不含空行):%21d| \n|行数为(含空行):%23d|'%(numrow,len(alist)))
    print('|单词数为:%29d|'%len(wordslist))
    print('+' + '-'*38 + '+')
    print('\n'*2)
    
    

def countasc(strname):
    # 输入纯字母字符串
    # 打印字母所占比例

    str1 = strname.lower()
    timeslist = [0]*26  #存放次数统计
    for i in str1:
        k = ord(i) - ord('a')
        timeslist[k] += 1

    lenstr1 = len(str1)
    print('{0:^38}'.format('统计部分2'))
    print('+' + '-'*38 + '+')
    for i in range(26):
        print('|字母%s出现次数为:%7d  占比%8.3f'%(chr(97 + i),timeslist[i],timeslist[i]*100/lenstr1)+'%|',sep='')
    print('+' + '-'*38 + '+')
    print('\n'*2)
    

def words(wordslist):
    ##输入单词表生成各单词字典wordsdict ={word1:times,word2:times2 ...}
    ##返回排序好(从大到小)的热词列表hotlist = [('the',27843)...]

    global wordsdict
    wordsdict = {}
    for i in wordslist:
        a = wordsdict.get(i)
        if a:
            wordsdict[i] = a + 1
        else:
            wordsdict[i] = 1

    hotlist = sorted(wordsdict.items(),key = lambda x:x[1],reverse = True)
    return hotlist

            

def printhotwords(hotlist,n=10,new = 0):
    ##美化打印hotlist中至多前n个元素


    k = min(len(hotlist),n)
    if new:
        print('{0:^46}'.format('热词排行榜(自定义版本)'))
    else:
        print('{0:^50}'.format('热词排行榜'))
    print('+' + '-'*50 + '+')
    for i in range(k):
        print('|热词排名第 %6d 位的是%10s  出现了%6d次'%( i+1 ,hotlist[i][0],hotlist[i][1])+'|',sep = '')
    print('+' + '-'*50 + '+')
    print('\n'*2)
        
        


def diyhotwords(wordsdict,notwantlist):
    ##输入单词情况字典和不要的单词列表
    ##返回去除不想要的单词的排好序的单词列表

    d = wordsdict
    for i in notwantlist:
        d.pop(i,'not in')
    return sorted(d.items(),key = lambda x:x[1],reverse = True)




if __name__ == '__main__':

    time1 = time.time()
    
    listgene(textname = 'bill.txt')
    countasc(ascstr)
    hotlist = words(wordslist) 
    printhotwords(hotlist,n=10)
    
    time2 = time.time()
    deltat2 = time2 - time1
    print('运行耗时%.2f秒'%deltat2)
    print('\n'*2)


    doit = input('是否屏蔽特定热词重新查看热词榜(输入其它视为否)\n请输入(Y/N):')
    while doit in 'yY':
        while True:
            notwant = input('输入屏蔽单词(列表、元组、集合或单个字符串):')
            if notwant.isalpha():
                notwantlist = [notwant]
                break
            try:
                notwant = eval(notwant)
                if isinstance(notwant,(list,tuple,set)):
                    notwantlist = list(notwant)
                    ajudge = True
                    for i in notwantlist:
                        if not isinstance(i,str):
                            ajudge = False
                            break
                    if ajudge:
                        break
                    print('格式错误,请重新输入')
                elif isinstance(notwant,str):
                    notwantlist = [notwant]
                    break
                else:
                    print('格式错误,请重新输入')
            except:
                print('格式错误,请重新输入')
        notwantlist = [i.lower() for i in notwantlist]
        ##得到notwantlist



        while True:
            try:
                n = int(input('查看列表前n位,数字n = '))
                break
            except:
                print('格式错误,请重新输入数字')


        print('\n'*2)
        printhotwords(diyhotwords(wordsdict,notwantlist),n,1)

                                       
        doit = input('是否继续屏蔽特定热(输入其它视为否)\n请输入词(Y/N):')  
    
    time3 = time.time()
    deltat3 = time3 - time1
    print()
    print('程序运行完毕,总运行时间%.2f秒'%deltat3)

