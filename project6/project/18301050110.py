#循环结构求解百鸡问题
a = []
def money_chicken_problem(money=100, num=100):
    for cock in range(0, num+1):
        for hen in range(0, num+1):
            if 5 * cock + 3 * hen + (num - cock - hen) / 3 == money:
                a.append (cock)
                a.append (hen)
                a.append (num - cock - hen)


if __name__ == '__main__':
    money_chicken_problem(money=100, num=100)

            
print('总共有%d个解' % (len(a)/3))
print('解1：鸡翁 %d 鸡母 %d 鸡雏 %d' % (a[0], a[1], a[2]))
print('解2：鸡翁 %d 鸡母 %d 鸡雏 %d' % (a[3], a[4], a[5]))
print('解3：鸡翁 %d 鸡母 %d 鸡雏 %d' % (a[6], a[7], a[8]))
print('解4：鸡翁 %d 鸡母 %d 鸡雏 %d' % (a[9], a[10], a[11]))


#列表解析法求解百鸡问题
b = []
result = [(x, y, 100 - x - y) for x in range(101) for y in range(101) \
              if 5 * x + 3 * y + (100 - x - y) / 3 == 100]
b.extend(result)

print('总共有%d个解' % (len(b)))
print('解1：鸡翁 %d 鸡母 %d 鸡雏 %d' % (b[0][0], b[0][1], b[0][2]))
print('解2：鸡翁 %d 鸡母 %d 鸡雏 %d' % (b[1][0], b[1][1], b[1][2]))
print('解3：鸡翁 %d 鸡母 %d 鸡雏 %d' % (b[2][0], b[2][1], b[2][2]))
print('解4：鸡翁 %d 鸡母 %d 鸡雏 %d' % (b[3][0], b[3][1], b[3][2]))
