maxnumber_of_jiwneg = int(100/5)
maxnumber_of_jimu = int(100/3)
#method 1
result1 = []
for i in range(maxnumber_of_jiwneg+1):
    for j in range(maxnumber_of_jimu+1):
        remaining_money = 100-5*i-3*j
        if remaining_money>=0 and i+j+remaining_money*3 == 100:
            number_chicken = remaining_money*3
            result1.append((i,j,number_chicken))
## method 2
result2 = [(i,j,100-(i+j)) for i in range(maxnumber_of_jiwneg+1) for j in range(maxnumber_of_jimu+1) if(100-5*i-3*j>=0 and i+j+(100-5*i-3*j)*3 == 100)]
print('方法1')
for i,solution in enumerate(result1):
    print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d'%(i+1,solution[0],solution[1],solution[2]))
print('方法2')
for i,solution in enumerate(result2):
    print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d'%(i+1,solution[0],solution[1],solution[2]))