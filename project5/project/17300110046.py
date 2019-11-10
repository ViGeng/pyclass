def cal_e():
    total = 0
    i = 0
    n = 1
    while  n > 10**(-10):
        total += n
        i += 1
        n *= (1/i)
    return total

y = cal_e()
print('e的值为：',y)
input()
