#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import project7_util as util

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化class_sheet
    class_sheet = dict()
    for item in range(total):
        key = util.get_id()
        name = util.get_name()
        score = util.get_score()
        class_sheet[key]=[name,score]
    #print(class_sheet)

    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    list_class_sheet = sorted(class_sheet.items(),key=lambda x:x[0])
    name_string = '姓名'
    exam_scores = '期末考试成绩'
    print('ID\t %-10s \t %-10s\n' % (name_string, exam_scores))
    for i in list_class_sheet:
        print('%s\t %-10s \t %-10s'%(i[0],i[1][0],i[1][1]))
    return list_class_sheet


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """

    list_class_sheet = sorted(class_sheet.items(),key=lambda x:(x[1][1],-x[0]),reverse=True)
    ##成绩相同的情况下按照学号从小到大排列
    name_string = '姓名'
    exam_scores = '期末考试成绩'
    print('ID\t %-10s \t %-10s\n' % (name_string, exam_scores))
    for i in list_class_sheet:
        print('%s\t %-10s \t %-10s'%(i[0],i[1][0],i[1][1]))
    return list_class_sheet

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
