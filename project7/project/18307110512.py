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
    keys = []
    values = []
    for _ in range(total):
        keys.append(util.get_id())
        value = [util.get_name(),util.get_score()]
        values.append(value)
    class_sheet = dict(zip(keys,values))

    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    class_sheet_list = []
    for key in class_sheet.keys():
        item = [key,class_sheet.get(key)[0],class_sheet.get(key)[1]]
        class_sheet_list.append(item)
    def takeID(elem):
        return elem[0]
    class_sheet_list.sort(key=takeID)
    print('%3s   %-15s   %-5s'%('ID','Name','Score'))
    for item in class_sheet_list:
        print('%3s   %-15s   %-5s'%(item[0],item[1],item[2]))
    
    
          
def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    class_sheet_list = []
    for key in class_sheet.keys():
        item = [key,class_sheet.get(key)[0],class_sheet.get(key)[1]]
        class_sheet_list.append(item)
    def takeScore(elem):
        return elem[2]
    class_sheet_list.sort(key=takeScore)
    print('%3s   %-15s   %-5s'%('ID','Name','Score'))
    for item in class_sheet_list:
        print('%3s   %-15s   %-5s'%(item[0],item[1],item[2]))

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

