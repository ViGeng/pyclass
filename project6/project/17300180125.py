count=0
result=[]
for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            if (x + y + z == 100) and (z % 3 == 0) and ((5*x + 3*y + z // 3) == 100):
                count+=1
                result.append((x,y,z))
print("总共有",count,"种解法")
for i in range(0,count):
    print("解法",i+1,":",'鸡翁%s 鸡母%s 鸡雏%s'%(result[i]))
#解法一：循环结构

result=[(x,y,z) for x in range(0,101)\
        for y in range(0,101)\
        for z in range(1,101)\
        if (x+y+z==100)\
        and (z%3==0)\
        and (5*x+3*y+z//3==100) ]
print("总共有",len(result),"种解法")
for i in range(0,len(result)):
    print("解法",i+1,":",'鸡翁%s 鸡母%s 鸡雏%s'%(result[i]))
#解法二：列表解析式
