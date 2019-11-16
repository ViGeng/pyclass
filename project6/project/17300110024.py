def one_hundred_qs_cir(heads=100, money=100):
    alist = []
    found = False
    for 鸡翁 in range(0, heads):
        for 鸡母 in range(0, heads):
            for 鸡雏 in range(0,heads):
                if 鸡翁 + 鸡母 + 鸡雏 == heads\
                   and 5 * 鸡翁 + 3 * 鸡母 + 1/3 * 鸡雏 == money:
                    alist.append([鸡翁, 鸡母, 鸡雏])
    print('循环结构\n总共有个%d解'%len(alist))
    n=1
    for i in range(len(alist)):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d'%\
              (n, alist[i][0], alist[i][1], alist[i][2]))
        n += 1
    if not alist:
        print('无解')
        
def one_hundred_qs_ana(heads=100, money=100):
    blist = [[鸡翁, 鸡母, 鸡雏] for 鸡翁 in range(0, heads)\
                                    for 鸡母 in range(0, heads)\
                                    for 鸡雏 in range(0, heads)\
                                    if 鸡翁 + 鸡母 + 鸡雏 == heads\
                   and 5 * 鸡翁 + 3 * 鸡母 + 1/3 * 鸡雏 == money]
    print('列表解析式\n总共有个%d解'%len(blist))
    m=1
    for i in range(len(blist)):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d'%\
              (m, blist[i][0], blist[i][1], blist[i][2]))
        m += 1
    if not blist:
        print('无解')

one_hundred_qs_cir()
print()
one_hundred_qs_ana()
input()
