a=1
i=1
x=1
while a/i>=10e-10:
    x=(x+a/i)
    a=a/i
    i=i+1
print ("e的值为",x)
