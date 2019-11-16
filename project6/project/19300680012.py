#解法一
s=[(x,y,100-x-y) for x in range(101) for y in range(101)\
   if 5*x+3*y+(100-x-y)/3==100]
l=len(s)
print("总共有%d个解"%l)
for i in range(1,l+1):
    print("解%d:鸡翁"%i,s[i-1][0],"鸡母",s[i-1][1],"鸡雏",s[i-1][2])

print() #空行
#解法二
s=[]
for x in range(101):
    for y in range(101):
        if 5*x+3*y+(100-x-y)/3==100:
            s.append((x,y,100-x-y))
l=len(s)
print("总共有%d个解"%l)
for i in range(1,l+1):
    print("解%d:鸡翁"%i,s[i-1][0],"鸡母",s[i-1][1],"鸡雏",s[i-1][2])
