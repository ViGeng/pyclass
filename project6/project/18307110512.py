#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

#method_A
result_list = []
for rooster in range(101):
    for hen in range(101):
        for chick in range(101):
            if ((rooster + hen + chick) == 100
                and (rooster * 5 + hen * 3 + chick / 3) == 100):
                    result = [rooster,hen,chick]
                    result_list.append(result)

print('总共有',len(result_list),'个解',sep='')
for i in range(1,(len(result_list)+1)):
    print(('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d')%(i,result_list[i-1][0],result_list[i-1][1],result_list[i-1][2]))
    
print()

#method_B
result_list = [[rooster,hen,chick] for rooster in range(101) for hen in range(101) for chick in range(101)
                   if rooster + hen + chick == 100
                       and rooster * 5 + hen * 3 + (100-rooster-hen) / 3 == 100]

print('总共有',len(result_list),'个解',sep='')
for i in range(1,(len(result_list)+1)):
    print(('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d')%(i,result_list[i-1][0],result_list[i-1][1],result_list[i-1][2]))
