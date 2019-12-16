#！/usr/bin/env python3
#  -*- coding：utf-8 -*-
import random
#import math

# def get_random_int():
#     '''此函数随机产生一个[1,100]范围内的整数'''
#     random_int = random.randint(1,100)random_int = random.randint(1,100)
#     return random_int

def guess_random_int():
    '''此函数随机产生一个[1,100]范围内的整数,此函数对用户输入做出判断'''
    random_int = random.randint(1,100)
    print(random_int)
    i = 0 
    while i < 4:
        try:
            input_ = input('您猜的数是？')
            guess_float = float(input_)
            if (guess_float > 100) or (guess_float < 1):
                print("请输入一个[1,100]范围的整数") 
                continue
            else:
                if random_int > guess_float:
                    print("您猜的数太小了！")
                    i += 1 
                    ok = 0   
                elif random_int < guess_float:
                    print("您猜的数太大了！")
                    i += 1
                    ok = 0
                else:
                    i = 4
                    ok = 1
                    print('您猜对了！')
            if i == 4 and ok == 0:
                print('您已经猜了4次，要猜的数是%d'%random_int) 
                get_answer = (input('继续游戏（Y/N）?...'))
                if get_answer == 'y' or get_answer == 'Y':
                    i = 0
                    random_int = random.randint(1,100)
                    print(random_int)
                else:
                    break
        except ValueError as e:
            print("请输入一个[1,100]范围的整数","invalid literal for int() with base 10: \'%s\'"%(input_)) 
        except Exception as e:
            print("请输入一个[1,100]范围的整数",'  ',type(e),e)
    return guess_random_int

if __name__ == '__main__':
    #print(get_random_int())
    #random_int = get_random_int()
    guess_random_int()