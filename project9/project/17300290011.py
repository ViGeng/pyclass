#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project9_util as util

def open_file():
    encoding = util.detect_encoding('fudan_history.txt')
    f = open('fudan_history.txt', encoding=encoding)
    return f

def count_valid_line(file):
    number = 0
    for line in file:
        if not line.isspace():
            number += 1
    return number

def add_number(file, line_number):

    new_file_name = util.nl_filename('fudan_history.txt')
    new_file = open(new_file_name, 'wt')

    number = 0
    digits = len(str(line_number))

    for line in file:
        if line.isspace():
            new_line = line
        else:
            number += 1
            new_line = "{0:{1:d}d} ".format(number, digits) + line
        new_file.write(new_line)


def main():
    f = open_file()
    line_number = count_valid_line(f)
    f.seek(0)
    add_number(f,line_number)

if __name__ == '__main__':
    main()
