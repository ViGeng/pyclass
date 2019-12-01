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
        class_sheet[util.get_id()]=[util.get_name(),util.get_score()]

        pass

    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    list = sorted(class_sheet.keys())
    print(format("ID","<10"), format("Name","<20"),format("Score","<10" ))
    for i in range(len(list)):
        print(format(list[i],"<10"),format(class_sheet[list[i]][0],"<20"),format(class_sheet[list[i]][1],"<10"))



    pass


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    def takeSecond(elem):
        return elem[1]
    class_sheet_new=[list(class_sheet.keys()),list(class_sheet.values())]
    class_sheet_new[1].sort(key=takeSecond)
    print(format("ID", "<10"), format("Name", "<20"), format("Score", "<10"))
    for i in range(len(class_sheet_new[1])):
        print(format(list (class_sheet.keys()) [list (class_sheet.values()).index (class_sheet_new[1][i])],"<10"),format(class_sheet_new[1][i][0],"<20"),format(class_sheet_new[1][i][1],"<10"))




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
