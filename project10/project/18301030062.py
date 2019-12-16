
#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""猜数游戏：计算机随机产生一个[1,100]范围内的数，
用户可以有4次机会来猜数，如果猜的数大或者小时都应该提示用户猜的数是偏大还是偏小。"""

def guessnumber():
    from random import randint 
    n = randint(1,100)
    while True:
        i = 0
        while i < 4:
            try:
                x = int(input("您猜的数是？"))
                if not(1 <= x <= 100):
                    print("请您输入一个[1，100]范围内的整数")
                else:
                    i += 1
                    if x > n:
                        print('您猜的数太大了！')
                    elif x < n:
                        print('您猜的数太小了！')
                    else:
                        print('您猜对了！')
                        break
            except Exception as e:
                print("请您输入一个[1,100]范围内的整数")
                print(e)
        ques = input('继续游戏(Y/N)?').upper()
        if ques != 'Y':
            break
    return
guessnumber()
