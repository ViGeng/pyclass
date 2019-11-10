jie = 1
sum = 1
i = 1
n=jie*i
while n <= 10**10:
    jie = jie*i
    sum = sum+1/jie
    i = i + 1
    n=jie*i
print(sum)
