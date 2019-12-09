def line_num(text):
    #获得源文件的encoding和新文件的名字，并且读取源文件内容
    import project9_util as pj
    encoding1 = pj.detect_encoding(text)
    print('源文件的encoding：%s'%encoding1)
    name = pj.nl_filename(text)
    print('写进文件名为：%s'%name)
    with open(text,'r') as file:
        text = file.read()

    #将加上行号的内容写进去
    text_lines = text.splitlines(keepends=True)
    n = 0
    with open(name,'w',encoding=encoding1) as f:
        print('新写的文件的encoding：%s' % f.encoding)
        for line in text_lines:
            line = line.replace(' ','')
            if line != '\n':
                n += 1
                f.write('%2d '%n)
                f.write(line)
            else:
                f.write(line)

    #显示新文件内容
    with open(name,'r') as file:
        text1 = file.read()
        print('文件内容为：')
        print(text1)

if __name__ == '__main__':
    text = 'fudan_history.txt'
    line_num(text)
