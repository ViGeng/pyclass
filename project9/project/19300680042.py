import project9_util
b=[]
with open('fudan_history.txt') as f:
    y=f.read()
    x=y.splitlines(keepends=True)
    for i in range(len(x)):
        if len(x[i])<=2:
            b.append(i)
    a=[item for item in x if len(item)>2]
    for i in range(len(a)):
        a[i]=str(i+1)+'  '+a[i]
    for item in b:
        a.insert(item,'\n')
    c=''.join(a)
s=project9_util.detect_encoding('fudan_history.txt')
a=project9_util.nl_filename('fudan_history.txt')
with open(a,'w',encoding=s) as fh:
    fh.write(c)
