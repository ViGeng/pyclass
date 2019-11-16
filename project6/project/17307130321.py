#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

#方法一
headers=100
money=100
found=False
x=list()
y=list()
z=list()
i=0
for male in range(0,headers+1):
    for female in range(0,headers+1):
        for children in range(0,34):
            if((male + female + 3 * children)==headers and (5 * male + 3 * female + children)==money):
                x.append(male)
                y.append(female)
                z.append(children*3)
                i=i+1
                found=True
                break
if not found:
    print('无解')


print('总共有%d个解' % (i))
for k in range(0,i):
    print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' % (k+1,x[k],y[k],z[k]))   
        
#方法二
result=[(male,female,children*3) for male in range(0,headers+1)for female in range(0,headers+1)for children in range(0,34)
        if((male + female + 3 * children)==headers and (5 * male + 3 * female + children)==money)]
n=len(result)
print('总共有%d个解' % (n))
for t in range(0,n):
    print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' % (t+1,result[t][0],result[t][1],result[t][2]))   
