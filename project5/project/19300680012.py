i=1 #n
s=0 #e
t=1 #1/n!
while t>10**(-10):
    s=s+t
    t=t/i
    i=i+1
else:
    print("e=",s)
