e=1
a=1
n=2
while a>=1e-10:
    e+=a
    a=a/n
    n+=1
print("e=",e)
