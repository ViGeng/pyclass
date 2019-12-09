

import project9_util as util
import string 



def text_plusnum(name='fudan_history.txt'):

    f = open(name,'r',encoding = util.detect_encoding(name))

    lineslist = f.readlines()

    k = 0
    newlines = []
    length = len(lineslist)
    maxn = len(str(length))
    for i in range(length):
        if lineslist[i].isspace():
            newlines.append(lineslist[i])
        else:
            k = k + 1
            newlines.append(str(k)+' '* (maxn + 1 -len(str(k)) ) + lineslist[i])

    f.close()

    f1 = open(util.nl_filename(name),'w',encoding =  util.detect_encoding(name))

    f1.writelines(newlines)

    f1.close()












if __name__=='__main__':

    

    text_plusnum()
