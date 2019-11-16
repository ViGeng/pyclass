
solution = 0
result = []
def pprint(alist):
    for i in range(0,len(alist)):
        print('%s%d%s %d %s %d %s %d'%('解',i+1,':鸡翁',alist[i][0],'鸡母',alist[i][1],'鸡雏',alist[i][2]))

if __name__ == '__main__':
    for roaster in range(0,101):
        for hen in range(0,101 - roaster):
            if 5 * roaster + 3 * hen + (100 - roaster - hen) / 3 == 100:
                solution = solution + 1
                answer = (roaster,hen,100 - roaster - hen)
                result.append(answer)
            
    print('%s%d%s'%('总共有',solution,'个解'))
    pprint(result)

    print()

    result2 = [(roaster,hen,100 - roaster - hen) for roaster in range(0,101) for hen in range (0,101 - roaster) if 5 * roaster + 3 * hen + (100 - roaster - hen) / 3 == 100]
    print('%s%d%s'%('总共有',solution,'个解'))
    pprint(result2)

