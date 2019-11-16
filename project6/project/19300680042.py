if __name__ == '__main__':
    money = 100
    total = 100
    i=1
    t=[]
    for male in range(0,total+1):
        for female in range(0,total+1):
            if (male*5 + female*3 + (total- male- female)/3 ==100):
                t.append([male,female,(total-male-female)])
                i = i+1
    m = len(t)
    print ('总共有%d个解'%m)
    for i in range (0,m):
        print ('解%d'%i,'：鸡翁',t[i][0],'鸡母',t[i][1],'鸡雏',t[i][2])


    s=[(x,y,z) for x in range(101) for y in range(101) for z in range(101)
    if 5*x+3*y+z/3==100 and x+y+z==100]
    l = len(s)
    print ('总共有%d个解'%l)
    for j in range (0,l):
        print ('解%d'%j,'：鸡翁',s[j][0],'鸡母',s[j][1],'鸡雏',s[j][2])
    
