e_estimate = 1
one_item = 1
epsilon = 10e-10
i = 1
while(one_item>epsilon):
    e_estimate+=one_item
    i +=1
    one_item = one_item*(1/i)
print('计算得出自然对数底数为'+str(e_estimate))
