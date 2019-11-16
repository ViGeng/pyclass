#方法一：循环
def sum():
    print ('总共有4个解')
    for g in range (0,20):     #公鸡最多20只*5=100元
        for m in range (0,33): #母鸡最多33只*3=99元
            x = 100 - g - m
            if 5*g + 3*m + x/3 == 100:
                print ('解：鸡翁%s 鸡母%s 鸡雏%s' %(g,m,x))


#方法二：列表        
def sum2():
    print ('总共有4个解')
    result = [(g,m,100-g-m) for g in range(0,20) for m in range(0,33) if (100-g-m)%3 == 0 and 5*g + 3*m +(100-g-m)//3 == 100]

    print ('解1：鸡翁%s 鸡母%s 鸡雏%s' %result[0])
    print ('解2：鸡翁%s 鸡母%s 鸡雏%s' %result[1])
    print ('解3：鸡翁%s 鸡母%s 鸡雏%s' %result[2])
    print ('解4：鸡翁%s 鸡母%s 鸡雏%s' %result[3])

if __name__ == '__main__':
    sum()
    sum2()