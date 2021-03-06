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
        # your code here....
        ID = util.get_id()
        name = str(util.get_name())
        score = util.get_score()
        class_sheet[ID] = [name,score]
        pass

    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    print('  ID  Name      Score')
    id_list = []
    for key in class_sheet:
        id_list.append(key)
    id_list.sort()
    for i in id_list :
        print('%4d  %-8s  %d' % (i,class_sheet[i][0],class_sheet[i][1]))
        
    pass


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    print('  ID  Name      Score')
    score_list = []
    for key in class_sheet:
        score_list.append(class_sheet[key][1])
    score_list.sort()    
    for score in score_list :
        for i in class_sheet:
            if class_sheet[i][1] == score :
                print('%4d  %-8s  %d' % (i,class_sheet[i][0],class_sheet[i][1]))

            
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
