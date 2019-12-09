#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import project9_util as util


def main():
    text = 'fudan_history.txt'
    list_ = []

    
    with open(text, mode ='r', encoding = util.detect_encoding(text)) as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if len(line.strip()) > 0:
                count += 1
                list_.append(str(count) + ' ' + line)
            else:
                list_.append('\n')

                
    with open(util.nl_filename(text), mode = 'w', encoding = util.detect_encoding(text)) as file:
        file.writelines(list_)        
        


if __name__ == '__main__':
    main()
