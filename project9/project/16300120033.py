import project9_util as util

a=util.detect_encoding('fudan_history.txt')
name=util.nl_filename('fudan_history.txt')
                       
with open ('fudan_history.txt','r',encoding=a) as file:
    b=file.readlines()
    b.remove(b[0])
    b0=[]
    c=1
    for i in b:
        if i != '\n':
            i=str(c)+" "+i
            c =c+1
        b0.append(i)
        b0.append('\n')

with open (name,'w',encoding=a) as f:
    f.writelines(b0)

    
    
    
    
