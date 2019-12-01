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
        # your code here....
        s_id = util.get_id()
        name = util.get_name()
        score = util.get_score()
        class_sheet[s_id] = [name, score]
        pass

    return class_sheet



def print_class_sheet(class_sheet):                   #!
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    print('%5s  %-15s %s' % (' ID', 'Name', 'Score'))
    for s_id in sorted(class_sheet):
        print('%5s  %-15s %s' % (s_id, class_sheet[s_id][0], class_sheet[s_id][1]))
    pass


def print_class_sheet_sorted(class_sheet):         #!
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    print('%5s  %-15s %s' % (' ID', 'Name', 'Score'))
    for s_id, (name, score) in sorted(class_sheet.items(),key=lambda x:x[1][1]):      #d.items()返回可迭代对象，元素为包括了(key,value)的元组
    #
        print('%5s  %-15s %s' % (s_id, name, score))
    pass
    # for i in enumerate(iterable):  #idx, element  #解包


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
