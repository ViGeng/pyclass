import os
import project9_util as util

def main():
    p = os.path.realpath('')
    filename = os.path.join(p,'fudan_history.txt')
    encoding = util.detect_encoding(filename)
    f = open(filename,'r',encoding = encoding)
    lines = list(f.readlines())

    file = util.nl_filename(filename)
    a = open(file,'x',encoding = encoding)

    i = 0
    n = 1

    while i < len(lines):
        if len(lines[i].strip()) != 0:
            lines[i] = '%2d  %s'%(n, lines[i])
            n += 1
        else:
            n = n
        i += 1
    a.writelines(lines)
    a.flush()

if __name__ == '__main__':
    main()
