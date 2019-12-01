#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
from project7_util import get_name
from project7_util import get_score
from project7_util import get_id
def get_class_sheet(total=25):
    class_sheet = dict()
    i=0
    for i in range(total):
        a=get_name(3,8)
        b=get_score()
        c=int(get_id())
        class_sheet[c]=[a,b]
        i=i+1
        pass

    return class_sheet


def print_class_sheet(class_sheet):
    print(" ID Name     Score")
    for u in sorted(class_sheet):
        print("%3.0d"%u,"%-8s"%class_sheet[u][0],class_sheet[u][1])
    pass


def print_class_sheet_sorted(class_sheet):
    print(" ID Name     Score")
    class_sheet_sorted={value[1]:[key,value[0]]for key,value in class_sheet.items()}
    for u in sorted(class_sheet_sorted):
        print("%3.0d"%class_sheet_sorted[u][0],"%-8s"%class_sheet_sorted[u][1],u)
    pass

def main():
    class_sheet = get_class_sheet(25)

    print()
    print('成绩单如下，按照ID排序\n')
    print_class_sheet(class_sheet)

    print()
    print('-'*50)
    print()
    print('成绩单如下，按照成绩排序\n')

    print_class_sheet_sorted(class_sheet)

if __name__ == '__main__':
    main()
