import project9_util as util

with open('fudan_history.txt','r',encoding=util.detect_encoding('fudan_history.txt'))\
     as f:
    i=1
    with open(util.nl_filename('fudan_history.txt'),'a',encoding=util.detect_encoding('fudan_history.txt')) as g:
        for lines in f:
            if lines.strip():
                g.write("%d  %s" % (i,lines))
                i+=1
            else:
                g.write('\n')
