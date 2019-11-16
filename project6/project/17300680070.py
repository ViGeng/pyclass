def main():
    ##方法一
    lista = []
    a = 0
    i = 0
    while a * 5 <= 100:
        for b in range(0,100//3+1):
            if 5 * a + 3 * b + (100-a-b) / 3 == 100:
                lista.append(a)
                lista.append(b)
                lista.append(100-a-b)
                i += 1
        a += 1

    print('%s%d%s'% ('总共有', i, '个解'))
    t = 1
    while t <= i:
        print('%s%d%s %d %s %d %s %d'%('解', t, ':鸡翁',lista[t*3-3], '鸡母', lista[t*3-2],
                                   '鸡雏', lista[t*3-1]))
        t += 1
    print()

    ##方法二
    listb = [[a, b, 100-a-b] for a in range(0, 100//5+1) for b in range(0, 100//3+1)
              if 5 * a + 3 * b + (100-a-b)/3 == 100]
    m = 1
    while m <= i:
        print('%s%d%s %d %s %d %s %d'%('解', m, ':鸡翁',listb[m-1][0], '鸡母', listb[m-1][1],
                                   '鸡雏', listb[m-1][2]))
        m += 1

if __name__ == '__main__':
    main()
