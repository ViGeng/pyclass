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
    for _ in range(total):
        a=util.get_id()
        b=util.get_name(min_chars=3, max_chars=8)
        c=util.get_score()
        class_sheet[a]=[b,c]
    pass
    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    sheet1=sorted(class_sheet.items(),key=lambda item:item[0])
    print(2*" "+"ID"+3*" "+"Name"+11*" "+"Score")
    for i in range(len(sheet1)):
        a=len(str(sheet1[i][0]))
        b=len(sheet1[i][1][0])
        print((4-a)*" "+str(sheet1[i][0])+3*" "+sheet1[i][1][0]+(15-b)*" "+str(sheet1[i][1][1]))
    pass


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    sheet2=sorted(class_sheet.items(),key=lambda item:item[1][1])
    print(2*" "+"ID"+3*" "+"Name"+11*" "+"Score")
    for i in range(len(sheet2)):
        a=len(str(sheet2[i][0]))
        b=len(sheet2[i][1][0])
        print((4-a)*" "+str(sheet2[i][0])+3*" "+sheet2[i][1][0]+(15-b)*" "+str(sheet2[i][1][1]))
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
