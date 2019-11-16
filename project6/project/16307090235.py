#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

"""今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。
凡百钱买鸡百只，问鸡翁、母、雏各几 何？
用一个列表保存所有解，最后再输出这些解。
求解部分用两种方法实现，第一种方法采用循环结构，
                        第二种方法采用列表解析（推导）式实现。
提示：可参考 3 选择与循环结构中的鸡兔同笼问题
"""

def chicken_1(amount=100, money=100):
    # 已知共有100只鸡，100钱
    found = False
    for cock in range(0, amount + 1):
        for hen in range(0, amount + 1):
            for chick in range(amount + 1):
                if (cock + hen + chick) == amount and (5 * cock + 3 * hen + 1/3 * chick) == money:
                    print('鸡翁%d只, 鸡母%d只, 鸡雏%d只' % (cock, hen, chick))
                    found = True
                    break
    if not found:
        print('无解')


def chicken_2(amount=100, money=100):
    # i = cock = 鸡翁
    result_list = []
    result_list = [(i, hen, amount-i-hen) for i in range (0, amount+1)  
           for hen in range(amount+1) if 5*i + 3*hen + (amount-i-hen)/3==100]
    result_list_append  = result_list.append([])

    print('总共有%d个解：' % (len(result_list)-1))   
    for i in range(1,len(result_list)):
        print('鸡翁%d只, 鸡母%d只, 鸡雏%d只'% ((result_list[i-1][0]),(result_list[i-1][1]),(result_list[i-1][2]))) 


if __name__ == '__main__':
    print('总共有4个解：')
    chicken_1()
    print('-' * 40)
    chicken_2()
    

    
