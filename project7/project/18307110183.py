#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


import random
import string


def get_name(min_chars=3, max_chars=8):
    """ 返回一个名字，长度介于min_chars和max_chars之间
    """
    VALID_CHARS = string.ascii_lowercase

    names = [random.choice(VALID_CHARS) for i in range(random.randint(min_chars,max_chars))]
    names[0] = names[0].upper()
    return ''.join(names)


def get_score():
    """ 返回一个分数，介于50和100之间
    """
    return random.randint(50,100)


ids_in_use = []


def get_id():
    """ 返回一个唯一的ID，在[1,999]之间
    """
    global ids_in_use    # 这一行可不要

    while True:
        s_id = random.randint(1, 999)
        if s_id not in ids_in_use:
            ids_in_use.append(s_id)
            return s_id


def get_class_sheet():
    sheet = dict()
    for num in range(10):
        lists = []
        names = get_name()
        scores = str(get_score())
        ids = str(get_id())
        lists = [names, scores]
        sheet[ids] = lists
    return sheet


def print_class_sheet(sheet):
    list_ids = sorted(list(sheet),key=lambda i: int(i))
    print('成绩如下，按照ID排序：')
    print()
    print('ID','Name','Score')
    for i in range(len(list_ids)):
        ids = list_ids[i]
        print(ids.ljust(5), sheet[ids][0].ljust(10),
              sheet[ids][1].ljust(5))


def print_class_sheet_sorted(sheet):
    list_ids = sorted(list(sheet),key=lambda i: int(sheet[i][1]))
    print('成绩如下，按照成绩排序：')
    print()
    print('ID'.ljust(5),'Name'.ljust(10),'Score'.ljust(10))
    for i in range(len(list_ids)):
        ids = list_ids[i]
        print(ids.ljust(5), sheet[ids][0].ljust(10),
              sheet[ids][1].ljust(10))   


if __name__ == '__main__':
    sheet = get_class_sheet()
    print_class_sheet(sheet)
    print()
    print('-'* 30)
    print()
    print_class_sheet_sorted(sheet)
    
