#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，问鸡翁、母、雏各几何？ 出自《张邱建算经》
用一个列表保存所有解，最后再输出这些解。
求解部分用两种方法实现，第一种方法采用循环结构，第二种方法采用列表解析（推导）式实现。
"""

def Print_Ans(Ans):
    print("总共有%d个解" % (len(Ans)))
    for i in range(0, len(Ans)):
        print("解%d：鸡翁 %d 鸡母 %d 鸡雏 %d" % (i + 1, *Ans[i]))

def Solution_Loop(Money=100, Num=100):
    Ans = []
    for Rooster in range(0, Money // 5 + 1):
        for Hen in range(0, (Money - Rooster * 5) // 3 + 1):
            Chicken = Num - Rooster - Hen
            if Rooster * 5 + Hen * 3 + Chicken / 3 == Money:
                Ans.append([Rooster, Hen, Chicken])
    Print_Ans(Ans)

def Solution_List(Money=100, Num=100):
    Ans = [[Rooster, Hen, 100 - Rooster - Hen]
           for Rooster in range(0, Money // 5 + 1)
           for Hen in range(0, (Money - Rooster * 5) // 3 + 1)
           if Rooster * 5 + Hen * 3 + (100 - Rooster - Hen) / 3 == 100]
    Print_Ans(Ans)

if __name__ == '__main__':
    print('方法一：循环方法')
    Solution_Loop()
    print('==================================')
    print('方法二：列表推导方法')
    Solution_List()
    
