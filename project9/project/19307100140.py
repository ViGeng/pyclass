import project9_util as p9

def add_num():
    with open(file,'r',encoding = '%s' % (p9.detect_encoding(file))) as f:
        text_list = f.readlines()
    t = ','.join(text_list).strip(' ').split(',')   
    count = 1
    l = []
    for i in t:
        if i == '\n':
            i = i
            l.append(i)
        else:
            i = ('%5.d\t'%(count)) + i
            count += 1
            l.append(i)
                
    return l

def new_text():
    new_l = add_num()
    with open(newfile,'w',encoding = '%s' % (p9.detect_encoding(file))) as n:
        n.writelines(new_l)
        
if __name__ == '__main__':
    file = 'fudan_history.txt'
    newfile = p9.nl_filename(file)
    add_num()
    new_text()
    file = 'project9_util.py'
    newfile = p9.nl_filename(file)
    add_num()
    new_text()
