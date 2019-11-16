#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
def main():

    aList = []
    for cock in range (0,101):
        for hen in range (0,101):
            chick = 100 - cock - hen
            if (cock * 5 + hen * 3 + chick / 3 == 100) and (chick % 3 == 0):
                print
                aList.append((cock, hen, chick))
                
    print("总共有%d个解"%(len(aList)))
    for j in range(len(aList)):
        print("解%d：鸡公%d 鸡母%d 鸡雏%d"%(j+1,aList[j][0],aList[j][1],aList[j][2]))


    b=[(x, y, 100-x-y) for x in range (0,101)
                        for y in range (0,101)
                        if (100-x-y) % 3 == 0
                        and 5 * x + y * 3 + (100-x-y)// 3 == 100]
    print("总共有%d个解"%(len(b)))
    for j in range(len(aList)):
        print("解%d：鸡公%d 鸡母%d 鸡雏%d"%(j+1,b[j][0],b[j][1],b[j][2]))


if __name__ == '__main__':
    main ()
