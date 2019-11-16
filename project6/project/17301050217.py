#循环结构实现列表保存所有解
def chicken_amount(number=100,money=100):
    _save = []
    found = False
    for male in range(0,number+1):
        for female in range(0,100-male+1):
            small = 100-male-female
            if 5*male + 3*female + small/3 == money:
                _save.append(male)
                _save.append(female)
                _save.append(small)
                found = True
    if not found:
        print('此题无解')
    return _save
# print(chicken_amount(number=100,money=100))



#列表推导式实现列表保存所有解
def chicken_amount():
    _save_=[(a,b,100-a-b) for a in range(101)
            for b in range(101-a)
            if 5*a+3*b+(100-a-b)/3==100]
    _save = [j for i in _save_
                    for j in i]
    return _save
#print(chicken_amount())


if __name__ =='__main__':
    m = chicken_amount()
    #上面两种实现得到的列表一摸一样，可以随便选一种
    solve = int(len(m)/3)
    print('总共%d有个解' % solve)
    for i in range(solve):
        print('解%d:鸡翁 %d  鸡母 %d 鸡雏 %d' % (int(i+1),m[3*i],m[3*i+1],m[3*i+2]))
    
    
















