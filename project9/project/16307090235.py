# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#给文本加行号 


import project9_util as util


encode_type = util.detect_encoding('fudan_history.txt')

def text_linenumber():
    with open('fudan_history.txt','r',encoding = encode_type) as file:
        line = file.readlines()
        i = 1
        z = []
        for a in range(1,len(line)):
            if line[a] == '\n':
                s = '\n\n'
                a += 1
            else:
                s = '  %d  %s\n'%(i,line[a])
                i += 1
                a += 1
            b = z.append(s)
          
        new_file = util.nl_filename('fudan_history.txt')
        text = open(new_file,'x',encoding = encode_type)
        new_file= text.writelines(z)
                

if __name__ == '__main__':
    text_linenumber()
    
