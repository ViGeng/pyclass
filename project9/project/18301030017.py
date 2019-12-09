import project9_util as p

text='fudan_history.txt'

with open(text,'r',encoding=p.detect_encoding(text)) as f :
    lines=f.readlines()
    i=0
    for line in lines:
        if line.strip()=='':
            print(line)
        else:
            i+=1
            line='{0}'.format(i)+' '*3+line
        print(line)
with open(p.nl_filename(text),'w') as fp:
    fp.writelines(lines)
    
