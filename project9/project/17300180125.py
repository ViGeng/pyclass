def newtxt(s,g):
    Lines=s.splitlines()
    count=[]
    for line in Lines:
        if not line:
            g.write('\n')
            count.append(1)
        else:
            i=Lines.index(line)+1
            format='%-2d %-s\n'
            g.write(format%(i-int(len(count)),line)) 

if __name__=='__main__':
    f=open('fudan_history.txt','r')
    s0=f.read()
    s=s0.strip()
    f.close()
    g=open('fudan_history_nl.txt','a')
    newtxt(s,g)
    g.close()

