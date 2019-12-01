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
    all_id = []
    all_name = []
    all_score = []
    name_score = []
    for i in range(total):
        # your code here....
        all_id.append(util.get_id())
        all_name.append(util.get_name())
        all_score.append(util.get_score())
    for i in range(total):
        name_score.append([all_name[i-1],all_score[i-1]])
    class_sheet.update(dict(zip(all_id,name_score)))
    return class_sheet
    

def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    sorted_sheet1 = dict(sorted(list(class_sheet.items()), key=lambda item:(item[0])))
    print('{:>4s}  {:<10s}    {:<10s}'.format('ID','Name','Score'))
    for key,value in sorted_sheet1.items():
        print('{:>4s}  {:<10s}    {:<10s}'.format(str(key),str(value[0]),str(value[1])))

def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    sorted_sheet2 = dict(sorted(list(class_sheet.items()), key=lambda item:(item[1][1])))    
    print('{:>4s}  {:<10s}    {:<10s}'.format('ID','Name','Score'))
    for key,value in sorted_sheet2.items():
        print('{:>4s}  {:<10s}    {:<10s}'.format(str(key),str(value[0]),str(value[1])))

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
