def add_line_number(text):
    import project9_util as util
    encoding = util.detect_encoding(text)
    file = open(text,encoding = encoding)
    alist = file.readlines()
    filename = util.nl_filename(text)
    newfile = open(filename,'w',encoding = encoding)
    n = 1
    for i in alist:
        if i.strip() == '':
           newfile.write(i) 
        else:
            newfile.write('%7d\t%s'%(n,i))
            n += 1
    file.close()
    newfile.close()

if __name__ == '__main__':
    text = 'fudan_history.txt'
    add_line_number(text)
    text = 'project9_util.py'
    add_line_number(text)
