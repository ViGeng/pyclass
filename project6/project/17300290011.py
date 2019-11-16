
def print_list(Ans):
    print("总共有%d个解" % (len(Ans)))
    for i in range(0,len(Ans)):
        print("解%d：鸡翁 %d 鸡母 %d 鸡雏 %d" % (i + 1, Ans[i][0], Ans[i][1], Ans[i][2]))


def Chicken_Loop(Money=100,Chicken=100):
    Ans = []
    for rooster in range(0,Money//5 + 1):
        for hen in range(0,Money//3 + 1):
            chick = Chicken - rooster - hen
            if (chick%3 == 0) and (5 * rooster + 3 * hen + chick/3 == Money):
                Ans.append([rooster,hen,chick])
    print_list(Ans)


def Chicken_list_comprehension(Money=100,Chicken=100):
    Ans = [[rooster,hen,Chicken - rooster - hen]
           for rooster in range(0,Money//5 + 1)
           for hen in range(0,Money//3 + 1)
           if 5 * rooster + 3 * hen + (Chicken - rooster - hen)/3 == Money
           ]
    print_list(Ans)


if __name__ == '__main__':
    Chicken_Loop()
    print('-' * 40)
    Chicken_list_comprehension()
    
    
