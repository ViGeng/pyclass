#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#Project7 作者：19级经济学院 应眺

import project7_util as util

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化class_sheet
    class_sheet = dict()
    for _ in range(total):
        class_sheet[util.get_id()]=[util.get_name(),util.get_score()]

    return class_sheet
    


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    print(' ID', 'Name    ', 'Score', sep = '\t')
    sorted_ids = sorted(class_sheet)
    for id in sorted_ids:
        print('%3i'%id, '%-8s'%class_sheet[id][0], class_sheet[id][1], sep = '\t')


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    print(' ID', 'Name    ', 'Score', sep = '\t')
    sorted_scores = sorted(class_sheet,key = lambda item:-class_sheet[item][1])
    #注：参考示例中成绩是按从低到高排的，但我认为从高到底排更合理
    for id in sorted_scores:
        print('%3i'%id, '%-8s'%class_sheet[id][0], class_sheet[id][1], sep = '\t')
    
    
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


