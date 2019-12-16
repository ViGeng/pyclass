import random


class RangeError(Exception):
    pass
class NumErorr(RangeError):
    def __init__(self,guess_number):
        self.guess_number=guess_number
    def __str__(self):
        return '您输入的整数不在[0,100]之间'

  
    
def G():
    N=1
    x=random.randint(0,100)
    try:
        guess_number=int(input('[{}]您猜的数是?'.format(N)))
        if guess_number not in range(0,100):
            raise NumError(guess_number)
    except NameError and ValueError and Exception :
        e=NameError and ValueError
        print('请输入一个[1,100]范围的整数',e)
        try:
            guess_number= int(input('[{}]您猜的数是?'.format(N)))
            if guess_number not in range(0,100):
                raise NumError(guess_number)
        except NameError and ValueError and Exception :
            e=NameError and ValueError
            print('请输入一个[1,100]范围的整数',e)
            try:
                guess_number= int(input('[{}]您猜的数是?'.format(N)))
                if guess_number not in range(0,100):
                    raise NumError(guess_number)
            except NameError and ValueError and Exception :
                e=NameError and ValueError
                print('请输入一个[1,100]范围的整数',e)
                guess_number= int(input('[{}]您猜的数是?'.format(N)))

    while(guess_number>x or guess_number<x):
        N+=1
        if guess_number>x:
            print('您猜的数太大了!')
        elif guess_number<x:
            print('您猜的数太小了!')
        try:
            guess_number=int(input('[{}]您猜的数是?'.format(N)))
            if guess_number not in range(0,100):
                raise NumError(guess_number)
        except NameError and ValueError and Exception :
            e=NameError and ValueError
            print('请输入一个[1,100]范围的整数',e)
            try:
                guess_number= int(input('[{}]您猜的数是?'.format(N)))
                if guess_number not in range(0,100):
                    raise NumError(guess_number)
            except NameError and ValueError and Exception :
                e=NameError and ValueError
                print('请输入一个[1,100]范围的整数',e)
                try:
                    guess_number= int(input('[{}]您猜的数是?'.format(N)))
                    if guess_number not in range(0,100):
                        raise NumError(guess_number)
                except NameError and ValueError and Exception :
                    e=NameError and ValueError
                    print('请输入一个[1,100]范围的整数',e)
                    guess_number= int(input('[{}]您猜的数是?'.format(N)))
        if guess_number==x:
            print('您猜对了!')
            break
        if N>=4:
            print('您已经猜了4次,要猜的数是{}'.format(x))
            break 
G()

a=input('继续游戏(Y/N)?...')
if a=='y' or 'Y':
    G()
else:
    pass
"""
活动周是第几届,主题是什么13
五道选择题作为平时成绩

辨析题,说明理由
联系实际的理论分析题
社会主义一个题目
经济学两个题目
劳动价值理论,剩余价值理论
其他的题目都是哲学的部分,
"""


    
