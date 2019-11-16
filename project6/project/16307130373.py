# coding = 'utf-8'

##方法一：采用循环结构
list1 = []
for cock in range(0,21):
    for hen in range(0,34):
        for chick in range(0,101):
            if (chick % 3) == 0 and (cock + hen + chick)== 100:
                if ((cock * 5) + (hen * 3) + (chick / 3)) == 100:
                    list1.append([cock, hen, chick])
                    
print('方法一：采用循环结构')
print("总共有%d个解"%len(list1),'\r')
for i in range(0,len(list1)):
    print('解%d:鸡翁%3d  鸡母%3d  鸡雏%3d\r'%((i + 1),int(list1[i][0]),int(list1[i][1]),int(list1[i][2])))


##方法二：采用列表解析（推导）式
list2 = [[cock, hen, chick] for cock in range(0,21) for hen in range(0,34)  for chick in range(0,101) if (chick % 3) == 0 and (cock + hen + chick)== 100  if ((cock * 5) + (hen * 3) + (chick / 3)) == 100]

print('\n方法二：采用列表解析（推导）式')
print("总共有%d个解"%len(list2),'\r')
for i in range(0,len(list2)):
    print('解%d:鸡翁%3d  鸡母%3d  鸡雏%3d\r'%((i + 1),int(list2[i][0]),int(list2[i][1]),int(list2[i][2])))
                                          
                        
    
