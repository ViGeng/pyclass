#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 7 成绩单打印
# 宋德夫（17307110044）

import project7_util as util

def get_class_sheet(total=25):
    
    class_sheet = dict()
    
    for x in range(total):
        key = util.get_id()
        value = [util.get_name(),util.get_score()]
        class_sheet[key] = value

    return class_sheet

def print_class_sheet(class_sheet):
    
    print(" " * 8 + "ID" + "\t" + "Name" + " " * 11 + "Score")

    for key in sorted(class_sheet.keys()):
        print(" " * (10 - len(str(key))) +
              str(key) +
              "\t" +
              class_sheet[key][0] +
              " " * (15 - len(class_sheet[key][0])) +
              str(class_sheet[key][1]))

def print_class_sheet_sorted(class_sheet):
    
    print(" " * 8 + "ID" + "\t" + "Name" + " " * 11 + "Score")

    strange_class_sheet = dict()

    for key in class_sheet.keys():
        strange_key = class_sheet[key][1]
        strange_value = [class_sheet[key][0],key]
        strange_class_sheet[strange_key] = strange_value

    for key in sorted(strange_class_sheet.keys()):
        print(" " * (10 - len(str(strange_class_sheet[key][1]))) +
              str(strange_class_sheet[key][1]) +
              "\t" +
              strange_class_sheet[key][0] +
              " " * (15 - len(strange_class_sheet[key][0])) +
              str(key))

def main():
    
    class_sheet = get_class_sheet(25)

    print()
    
    print("成绩单如下，按照ID排序\n")
    print_class_sheet(class_sheet)

    print()
    print("-" * 50)
    print()
    
    print("成绩单如下，按照成绩排序\n")
    print_class_sheet_sorted(class_sheet)

    print()

if __name__ == "__main__":
    main()

