result = []
for cocks in range(0, 101):
    for hens in range(0, 101):
        for chickens in range(0,101):
            if (cocks + hens + chickens) == 100 and (5 * cocks + 3 * hens + chickens / 3) == 100:
               result.append((cocks,hens,chickens))
               print('鸡翁%d,母鸡%d,鸡雏%d' % (cocks,hens,chickens))



number, money = 100, 100
result = [(cocks, hens, chicks ) for cocks in range(101) for hens in range(101) for chicks in range(101)
            if int( cocks * 5 + hens * 3 + chicks / 3) == 100 and chicks % 3 == 0 and cocks + hens + chicks == 100]
print('鸡翁%d,母鸡%d,鸡雏%d' % (cocks,hens,chickens))


