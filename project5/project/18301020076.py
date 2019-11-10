p=1
e=2
for i in range(1,100):
    p *= i+1
    e=e+1/p
    if 1/p<10E-10:break           #限定精度
print("e=",e)
