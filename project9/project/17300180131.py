import project9_util as pr

linenumber=0

if __name__=='__main__':
    
    filename=input('请输入要打开的文件名\n')
    typeofname = pr.detect_encoding(filename)
    newname = pr.nl_filename(filename)
    
    file = open(filename,encoding=typeofname)
    lines = file.readlines()
    
    with open(newname,'a',encoding=typeofname) as f:
        for line in lines:
            if len(line.strip()) == 0:
                f.write(line)
            else:
                linenumber+=1
                sss=str(linenumber)+'  '
                f.write(sss+line)
            
