#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 9 给文本文件加上行号
# 宋德夫（17307110044）

import project9_util as util

def line_number():
    
    filename = "fudan_history.txt"
    
    with open(filename, encoding =
              util.detect_encoding(filename)) as file_object:
        contents = file_object.read()
        
    contents = contents.strip()
    
    contents = contents.split("\n")

    string = ""
    
    x = 1
        
    for content in contents:
        if content != "":
            string += str(x) + "\t" + content + "\n\n"
            x += 1
        else:
            string += "\n\n"

    string = string.rstrip()
    
    filename2 = util.nl_filename("fudan_history.txt")
    
    with open(filename2, "w", encoding =
              util.detect_encoding(filename)) as file_object:
        file_object.write(string)

def main():
    
    line_number()

if __name__ == "__main__":
    main()
