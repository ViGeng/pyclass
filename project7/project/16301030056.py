#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import random
import string

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
s = []
d1 = {}
while len(s) < 25:
       s_id = random.randint(1, 999)
       VALID_CHARS = string.ascii_lowercase
       names = [random.choice(VALID_CHARS) for i in range(random.randint(3,8))]
       names[0] = names[0].upper()
       p = random.randint(50,100)
       d1.update({s_id:[''.join(names), p]})
       s.append(d1)
print('ID','     ','Name','     ','Score')
def sort_by_name_age(item):
    return item[s_id]
print(sorted(s, key=sort_by_name_age))


def sort_by_name_age(item):
    return item[s_id]
print(sorted(s, key=sort_by_name_age))


def print_class_sheet_sorted(item):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    return item[p]
print(sorted(s, key=print_class_sheet_sorted))

def main():
    class_sheet = get_class_sheet(25)

    print()
    print('成绩单如下，按照ID排序\n')
    print_class_sheet(item)

    print()
    print('-'*50)
    print()
    print('成绩单如下，按照成绩排序\n')

    print_class_sheet_sorted(item)

if __name__ == '__main__':
    main()
