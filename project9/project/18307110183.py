#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import project9_util as util


def file_reader(file,encoding):
    with open(file,'r',
              encoding = encoding) as file:
        list_1 = file.readlines()
    return list_1


def file_writer(name,list_text,encoding):
    with open(name,'w',
              encoding = encoding) as file:
        i = 0
        for text in list_text:
            flag = False
            for letter in text:
                if letter not in ['\n',' ','\t']:
                    flag = True
                    break
            if flag:
                i += 1
                file.write('{0:d}\t{1:s}'.format(i,text))
            else:
                file.write('\t\t{0:s}'.format(text))
            file.write('\n')
                

def main():
    encoding = util.detect_encoding('fudan_history.txt')
    name = util.nl_filename('fudan_history.txt')
    list_1 = file_reader('fudan_history.txt',encoding)
    file_writer(name,list_1,encoding)
    

if __name__ == '__main__':
    main()
