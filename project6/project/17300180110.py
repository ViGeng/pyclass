def f1():
    result=[[x,y,100-x-y] for x in range(0,101) for y in range(0,101) if 5*x+3*y+(100-x-y)/3==100]
    return result

def f2():
    result_otherway=[]
    for x in range(0,101):
        for y in range(0,101):
            if 5*x+3*y+(100-x-y)/3==100:
                result_otherway.append([x,y,100-x-y])
    return result_otherway

def my_print(list_):
    print('总共有%d个解' % len(list_))
    for i in range(0,len(list_)):
        print('解%d: 鸡翁  %d 鸡母 %d 鸡雏  %d' % (i+1,list_[i][0],list_[i][1],list_[i][2]))
        
if __name__ == '__main__':
    result=f1()
    result_otherway=f2()
    my_print(result)
    my_print(result_otherway)

    
