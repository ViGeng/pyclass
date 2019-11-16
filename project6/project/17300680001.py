#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def printchick(xlist):
    print('%s%d%s'%('总共有',len(xlist),'个解'))
    for i in range (len(xlist)):
        print('%s%d%s%s %d %s %d %s %d'%('解',i+1,':','鸡翁',xlist[i][0],'鸡母',xlist[i][1],'鸡雏',xlist[i][2]))




if __name__ == '__main__':
    alist = []
    for father in range(0,101):
        for mother in range(0,101 - father):
            if 5 * father + 3 * mother + (100 - father - mother) / 3 == 100:
                alist.append((father,mother,100 - father - mother))
    printchick(alist)

    print()
    blist = [(father,mother,100 - father - mother) for father in range(0,101) for mother in
             range(0,101 - father) if 5 * father + 3 * mother + (100 - father - mother) / 3 == 100]
    printchick(blist)
