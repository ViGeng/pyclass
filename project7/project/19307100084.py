#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
import string

def pirnt_scores(domains):
    count=0
    for domain in domains:
        print(domain,end='\t')
        count+=1
        if count % 5 == 0:
            print()
        if count % 5 != 0:
            print()

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
        s_id = get_id()
        class_sheet[s_id]= [get_name(),get_score()]
        pass

    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    print('%5s\t%-10s\t%-5s' % ('ID', 'Name', 'Score'))
    for key in sorted(class_sheet): 
        print('%5d\t%-10s\t%-5d' % (key,class_sheet[key][0], class_sheet[key][1]))
    pass

def key_domain(item):
    return item[1][1]

def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    sorted_item = sorted(class_sheet, key=lambda item:(class_sheet[item][1],class_sheet[item][0]))
    print('{:>5s}\t{:<10s}\t{:<5s}'.format('ID', 'Name', 'Score'))
    for item in sorted_item: 
        print('{:>5}\t{:<10s}\t{:<5}'.format(item, *class_sheet[item]))
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


