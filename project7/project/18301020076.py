#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


from project7.project.project7_util import get_id
from project7.project.project7_util import get_name
from project7.project.project7_util import get_score

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化class_sheet
    class_sheet = dict()
    for i in range(total):
        class_sheet[get_id()]=[get_name(),get_score()] 

    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    for id in sorted(class_sheet.keys()):
            print('%5s %-10s %-5s' %(id,class_sheet[id][0],class_sheet[id][1]))
    pass

def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    list=[]
    for k,v in class_sheet.items():
        n=v[0]
        s=v[1]
        list.append([s,k,n])
    list_sorted=sorted(list)
    for i in range(25):
        id=list_sorted[i][1]
        name=list_sorted[i][2]
        score=list_sorted[i][0]
        print('%5s %-10s %-5s' %(id,name,score))
    pass     


    	
def main():
    class_sheet = get_class_sheet(25)
    
    print('成绩单如下，按照ID排序\n')
    print('%5s %-10s %-5s' % ("ID","Name","Score")) 
    print_class_sheet(class_sheet)

    print('-'*50)
    print()
    print('成绩单如下，按照成绩排序\n')
    print('%5s %-10s %-5s' % ("ID","Name","Score"))
    print_class_sheet_sorted(class_sheet)
    

  
if __name__ == '__main__':
    main()
    

