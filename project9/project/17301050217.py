def add_file_linenumber(file='fudan_history.txt'):
    f = open(file,'r')
    num = 0
    b = []
    for item in f.readlines():
        
        if item == '\n':
            num = num
            b.append(item)
        else:
            new_line = '    {}  '.format(num) + item
            b.append(new_line)
            num+=1
    f.close()
    fh = open('fudan_history_nl.txt','w')
    fh.writelines(b[1:]) 
    
    fh.close()
    return 

if __name__ == '__main__':
    
       add_file_linenumber(file='fudan_history.txt')     
         
        
