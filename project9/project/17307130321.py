#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project9_util as util
text='fudan_history.txt'
encoding=util.detect_encoding(text)

text1=open('fudan_history.txt','r')
textlist=text1.readlines()

linenumber=1
for i in range(len(textlist)):
   if ' ' in textlist[i] or textlist[i]=='\n':
      pass
   else:
       textlist[i]=str(linenumber)+' '+textlist[i]
       linenumber += 1

name=util.nl_filename('fudan_history.txt')

f=open(name,'w')
for k in range(len(textlist)):
    f.write(textlist[k])
f.close()









        
        
        
    

