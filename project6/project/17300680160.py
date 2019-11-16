#!/usr/bin/python3
 
#方法一
count = 0
result_chr = ""
for x in range(0, 20):                     
    for y in range(0, 33):          
        z = 100 - x - y                    
        if (z%3 == 0) and (5*x + 3*y + z/3 == 100):
            count += 1   
            result_chr = result_chr + '解%d：鸡翁 %d 鸡母 %d 鸡雏 %d'%(count, x, y, z) + '\n'
            continue

print('共有%d个解:'%count)
print(result_chr)

#方法二
count=0
result = [(x,y,100-x-y) for x in range(0, 20) for y in range(0,33)
		if ((100-x-y)%3 == 0) and (5*x + 3*y + (100-x-y)/3 == 100)]
print("共有%s个解"%len(result))
for x,y,z in result:
	count+=1
	print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d'%(count, x, y, z))
	