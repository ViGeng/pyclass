from project9_util import *
import codecs


def getFile():
    infile = input('请输入需要添加行号的文件名：')
    return infile


def lineNum(infile):
    outfile = nl_filename(infile)
    outf = codecs.open(outfile,'w',encoding=detect_encoding(infile))
    inf = open(infile,'r',encoding='gbk')
    lines = inf.readlines()
    n = 0 
    for t in lines:
        if t.split() == []:
            outf.write('\n')
        else:
            n = n + 1
            outf.write('%d  %s' % (n,t))
    inf.close()
    outf.close()

def main():
    infile = getFile()
    print(detect_encoding(infile))
    lineNum(infile)

if __name__ == '__main__':
 main()


open('fudan_history.txt','r')
