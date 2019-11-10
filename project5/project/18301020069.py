a=1
e=1
for i in range(1,100)
    a=a*i
    j=1/a
    e=e+j
    if a>=10**10:break
print("e=",e)
