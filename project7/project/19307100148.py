
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
    for _ in range(total):
        class_sheet[get_id()] = [get_name(),get_score()]

    return class_sheet
                               
    

def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    print("ID\tName\tSocre\t")
    for i in sorted(class_sheet.keys()):
        print("%s\t%s\t%s\t"% (i,class_sheet[i][0],class_sheet[i][1]))

        
def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐 
    """
    print("ID\tName\tSocre\t")
    for k,v in sorted(class_sheet.items() , key = lambda x:x[1][1]):
        print("%s\t%s\t%s\t" % (k,*v))
    
        
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
