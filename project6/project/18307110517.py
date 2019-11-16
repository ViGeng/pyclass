#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def rooster_hen_chick_hundred(num=100,coins=100):
    found = False
    results = []
    for roosters in range(0,num // 5):
        for hens in range(0,num // 3):
            chicks = 100 - roosters - hens
            if (chicks%3 == 0) and (5 * roosters+3 * hens + chicks / 3 == 100):
                results.append((roosters,hens,chicks))
                found = True
                break
    print('总共有%d个解' % len(results))
    for ans in results:
        print('解%d:' % (results.index(ans) + 1),end='')
        print('鸡翁:%d 鸡母:%d 鸡雏:%d' % ans)
    if not found:
        print('无解')


def rooster_hen_chick_hundred2(num=100,coins=100):
    results=[(roosters,hens,chicks) for roosters in range(num // 5) for hens in range(num // 3) for chicks in range(num * 3)
       if chicks%3 == 0 and 5 * roosters + 3 * hens + chicks / 3 == 100 and roosters + hens + chicks == 100]
    if (results ==''):
        print('无解')
    else:
        print('总共有%d个解' % len(results))
        for ans in results:
            print('解%d:' % (results.index(ans) + 1),end='')
            print('鸡翁:%d 鸡母:%d 鸡雏:%d' % ans)
            
              
if __name__ == '__main__': 
    rooster_hen_chick_hundred()
    print()
    rooster_hen_chick_hundred2()
