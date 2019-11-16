def calculate_chicken(count=100, money=100):
    res = []
    for rooster in range(int(count/5)+2):
        for hen in range(int(count/3)+2):
            for chick in range(count+1):
                if rooster + hen + chick == 100 and rooster * 5 + hen * 3 + chick / 3 == 100:
                    res.append((rooster, hen, chick))
    l = len(res)
    if l == 0:
        print('无解')
        return None
    else:
        print('总共有%d个解' %l)
        for i in range(l):
            print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' %(i+1, res[i][0], res[i][1], res[i][2]))
        return res

def calculate_chicken2(count=100, money=100):
    res = [(i, j, count-i-j) for i in range(int(count/5)+2) for j in range(int(count/3)+2)
           if i*5 + j*3 + (count-i-j)/3 == money]
    l = len(res)
    if l == 0:
        print('无解')
        return None
    else:
        print('总共有%d个解' % l)
        for i in range(l):
            print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' % (i + 1, res[i][0], res[i][1], res[i][2]))
        return res
    return res


print('--------------------------')
print('循环结构计算结果：')
calculate_chicken(100, 100)
print('\n\n--------------------------')
print('列表生成式计算结果：')
calculate_chicken2(100, 100)
