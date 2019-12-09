#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from project9_util import detect_encoding, nl_filename

def main(file):
    encoding = detect_encoding(file)
    new_file = nl_filename(file)

    with open(file, 'r', encoding=encoding) as f:
        lines = f.readlines()

    with open(new_file, 'w', encoding=encoding) as f:
        i = 1
        for line in lines:
            if not line.isspace():
                f.write('{} {}'.format(i,line))
                i = i + 1
            else:
                f.write(line)

if __name__ == '__main__':
    main('fudan_history.txt')
    
