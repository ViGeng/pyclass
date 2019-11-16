answer = []
number = 0
for a in range(20):
    for b in range(0,100,3):
        c=100-a-b
        if 5*a+b/3+3*c ==100 and c>=0:
            answer.append([a,c,b])
            number +=1
print('总共有',number,'个解')
for i in range(number):
    print('解',i+1,'：鸡翁 ',answer[i][0],' 鸡母 ',answer[i][1],' 鸡雏 ',answer[i][2])
