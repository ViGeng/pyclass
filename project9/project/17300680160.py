#  -*- coding: utf-8 -*-

def detect_encoding(text):

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

    if name.endswith(('.txt', '.py')):
        dot_pos = name.rindex('.')
        return name[0:dot_pos] + '_nl' + name[dot_pos:]
    else:
        return name + '_nl'

if __name__ == '__main__':
    print('%s-->%s: %s' % (__file__, nl_filename(__file__), detect_encoding(__file__)))

    text = 'fudan_history.txt'
    print('%s-->%s: %s' % (text, nl_filename(text), detect_encoding(text)))


    with open(text,'r',encoding=detect_encoding(text))as fp:
        lines=fp.readlines() 
        line_index=1
    for index,line in enumerate(lines):
        if line in ['\n','\r\n'] or line.strip() == "":
            pass
        else:
            newLine=str(line_index)+' '+line 
            line_index+=1
            lines[index]=newLine
        with open(nl_filename(text),'w')as fp:  
            fp.writelines(lines)
