#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""首先随机产生一个班级的成绩单，
然后按照学生 ID 的先后顺序打印成绩单，
最后按照成绩排名 的先后顺序打印成绩单
"""
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
        

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化class_sheet
    class_sheet = dict()
    for _ in range(total):
        # your code here....字典：{s_id:[name,score]}
        # d[key]=value:
        s_id = get_id()
        class_sheet[s_id] = [get_name(), get_score()]
        
    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    print('%8s\t%-8s\t%-8s' % ('ID', 'Name', 'Score'))

    for key in sorted(class_sheet): 
        print('%8s\t%-8s\t%-8s' % (key,class_sheet[key][0], class_sheet[key][1]) )


def sort_score(item):
    return item[1][1]


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    sorted_item = sorted(class_sheet.items(),key = sort_score)     
    print('%8s\t%-8s\t%-8s' % ('ID', 'Name', 'Score'))

    for item in sorted_item: 
        print('%8s\t%-8s\t%-8s' % (item[0],item[1][0],item[1][1]))
    


def main():
    class_sheet = get_class_sheet(10)

    print()
    print('成绩单如下，按照ID排序：\n')
    print_class_sheet(class_sheet)

    print()
    print('-'*30)
    print()
    print('成绩单如下，按照成绩排序：\n')

    print_class_sheet_sorted(class_sheet)

if __name__ == '__main__':
    main()
