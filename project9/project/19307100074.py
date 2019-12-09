import project9_util 
text = 'fudan_history.txt'
code = project9_util.detect_encoding(text)
f = open('fudan_history.txt', mode='r+', encoding=code)
s = f.readlines()
newname = project9_util.nl_filename('fudan_history.txt')
f1 = open(newname,mode='w',encoding=code)
a=1
for i in s:
    if len(i.strip())==0:
        a=a
        f1.write(i)
    else:
        f1.write(str(a)+i)
        a+=1

f.close()
f1.close()


