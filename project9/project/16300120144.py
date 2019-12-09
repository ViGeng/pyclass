import project9_util as util

def add_linenumber(text):
    encoding = util.detect_encoding(text)
    nl_name = util.nl_filename(text)
    
    f = open(text, 'r',encoding = encoding)
    nl_f = open('%s'% nl_name,'w',encoding = encoding)
    lines = f.readlines() 
    n=0

    for line in lines:
        ts_line = line.strip()
        if len(ts_line):
            n+=1
            nl_f.write('%s.'% n + line + '\n')   
        else:
            nl_f.write('\n') 
                  
    f.close()
    nl_f.close()
    return text
    
if __name__ == '__main__':
    text = 'project9_util.py'
    add_linenumber(text)
    
    text = 'fudan_history.txt'
    add_linenumber(text)
    
    
