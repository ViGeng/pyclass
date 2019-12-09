
def detect_encoding(text):
    """探测文件的编码方式
    参数：文件名， 返回探测到的编码方式
    """

    encodings = 'ASCII', 'UTF-8', 'GBK'

    for encoding in encodings:
        try:
            with open(text, encoding=encoding) as f:
                f.read(100)
            break
        except UnicodeDecodeError:
            pass
    return encoding

def nl_filename(name):
    """ 返回一个新的文件名，传递的参数name为文件名
    """

    if name.endswith(('.txt', '.py')):
        dot_pos = name.rindex('.')
        return name[0:dot_pos] + '_nl' + name[dot_pos:]
    else:
        return name + '_nl'



if __name__ == '__main__':
    print('%s-->%s: %s' % (__file__, nl_filename(__file__), detect_encoding(__file__)))
    text = 'fudan_history.txt'
    print('%s-->%s: %s' % (text, nl_filename(text), detect_encoding(text)))

    file = open(text, 'r')
    next(file)
    lines = file.readlines()
    file.close()
    n = 0
    with open( nl_filename(text), 'a',encoding=detect_encoding(text))as f:

        for line in lines:
            if line in ['\n','\r\n']:
                f.write(line)
            else:
                n=n+1
                f.write(str(n) + ' ' + line)
    f.close()






