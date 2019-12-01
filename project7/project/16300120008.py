#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
import string


def getName(min_chars = 3, max_chars = 8):
    """ 返回一个名字，长度介于min_chars和max_chars之间
    """
    VALID_CHARS = string.ascii_lowercase

    names = [random.choice(VALID_CHARS) for i in range(random.randint(min_chars,max_chars))]
    names[0] = names[0].upper()
    return ''.join(names)

def getScore():
    """ 返回一个分数，介于50和100之间
    """ 
    return random.randint(50,100) 


ids_in_use = [] #用于存放已经使用过的id

def getId():
    """ 返回一个唯一的ID，在[1,999]之间
    """
    global ids_in_use

    while True:
        s_id = random.randint(1,999)
        if s_id not in ids_in_use:
            ids_in_use.append(s_id)
            return s_id


def getClassSheet(total = 25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。 
    采用dict来纪录学生成绩单，每个学生包含唯一标识学生的ID、姓名和期末考试成绩
    可以调用上面提供的get_id()、get_name()、get_score来获得学生的信息。 
    """
    # 初始化class_sheet 
    class_sheet = dict() 
    for i in range(total): #for 循环
        class_sheet[getId()] = (getName(),getScore())
        # your code here.... 
        pass 

    return class_sheet


def printClassSheet(class_sheet,total = 90):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    for i in range(total):
        Sorted_Id = sorted(class_sheet.items())
        print('%5s\t%-10s\t%3d' %(Sorted_Id[i][0],Sorted_Id[i][1][0],Sorted_Id[i][1][1]))
        pass
    return(printClassSheet)

def key_func(item):
    return item[1][1]
def printClassSheetSorted(class_sheet,total=90):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    # your code here....
    Sorted_Score = sorted(class_sheet.items(),key = key_func)
    for i in range(total):
        print('%5s\t%-10s\t%3d' %(Sorted_Score[i][0],Sorted_Score[i][1][0],Sorted_Score[i][1][1]))
    pass     

def main():
    class_sheet = getClassSheet(20)

    print()
    print('成绩单如下，按照ID排序\n') 
    printClassSheet(class_sheet,20)

    print() 
    print('*'*50)
    print()
    print('成绩单如下，按照成绩排序\n') 
    
    printClassSheetSorted(class_sheet,20)

if __name__ == '__main__':
    main()
    

