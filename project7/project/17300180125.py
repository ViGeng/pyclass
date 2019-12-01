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
    for i in range(total):
        key=util.get_id()
        value=[util.get_name(min_chars=3, max_chars=8),util.get_score()]
        class_sheet[key]=value
        
    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    list1=sorted(class_sheet)
    dict1=dict()
    print('%-5s'%"ID",'\t','%-8s'%"Name",'\t','%-5s'%"Score",end='\n')
    for k in list1:
        dict1[k]=class_sheet[k]
    for key in dict1:
        print('%-5s'%key,'\t','%-8s'%dict1[key][0],'\t','%-5s'%dict1[key][1],end='\n')

def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    list2=sorted(class_sheet.items(),key=lambda item:item[1][1])
    dict2=dict()
    print('%-5s'%"ID",'\t','%-8s'%"Name",'\t','%-5s'%"Score",end='\n')
    
    for j in list2:
        dict2[j[0]]=j[1]
    for key in dict2:
        print('%-5s'%key,'\t','%-8s'%dict2[key][0],'\t','%-5s'%dict2[key][1],end='\n')
 

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

