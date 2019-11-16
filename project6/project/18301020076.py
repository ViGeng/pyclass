"""百鸡问题。假设用百元买百鸡"""

print("法一：")#循环结构
for x in range(0,20):       
	for y in range(0,33):
		z=100-x-y
		if(x*5+y*3+z/3==100)and(z%3==0):
			print("鸡翁",x,"鸡母",y,"鸡雏",z)

print("法二：")                          #列表解析式
heads,money=100,100
result=[(x,y,100-x-y) for x in range(heads+1)
			for y in range(heads+1)
                                if x*5+y*3+(100-x-y)/3 ==100]
print("共有%d个解，鸡翁,鸡母,鸡雏,集合为"%len(result),result)
