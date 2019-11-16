def number_chickens(headers=100,money=100):
    #百鸡百钱问题,假设有100只鸡，需要100钱
    #methods是所有解的集合,counters是计数器,solutions是最后引用函数赋予的变量
    found = False
    methods = []
    counters = 0
    for cocks in range(0,int(headers/5+1)):
        for hens in range(0,int(headers/3+1)):
            for chickens in range(0,headers*3+1):
                if cocks + hens + chickens == headers and (cocks*5 + hens*3 + chickens/3) == money:
                    # print("鸡翁 %d 鸡母 %d 鸡雏 %d" % (cocks,hens,chickens))
                    counters+=1
                    methods.append("解%d: 鸡翁 %d 鸡母 %d 鸡雏 %d" % (counters,cocks, hens, chickens))
                    found = True
                    break
    return methods


solutions = number_chickens()
print("总共有%d个解" % (len(number_chickens())))
for solution in solutions:
    print(solution)

