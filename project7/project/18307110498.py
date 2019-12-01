import project7_util as util

def get_class_sheet(total=25):
    """ 获得某个班级的学生成绩单，学生总人数缺省为25人，最终返回生成的成绩单。
    采用dict来纪录学生成绩单，包含唯一标识学生的ID、姓名和期末考试成绩，具体而言
    key为学生的ID，value为[姓名,成绩]，比如{285:['Stone', 99], 297:['Idle', 90]}
    可以调用上面提供的get_id()、get_name()、get_score来随机生成学生的相关信息。
    """
    # 初始化class_sheet
    class_sheet = dict()
    for x in range(total):
        _id = util.get_id()
        name = util.get_name(min_chars=3, max_chars=8)
        score = util.get_score()
        class_sheet.setdefault(_id,[]).append(name)
        class_sheet.setdefault(_id,[]).append(score)
        # your code here....
    return class_sheet


def print_class_sheet(class_sheet):
    """ 打印成绩单，按照ID排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    y = sorted(class_sheet.items(),key =lambda item:item[0])
    print('%-5s  %-10s %-10s'%('ID','Name','Score'))
    for i in y:
        print('%-5d  %-10s %-10d'%(i[0],i[1][0],i[1][1]))
    
    # your code here....
    pass


def print_class_sheet_sorted(class_sheet):
    """ 打印成绩单，按照成绩排序，每行包括ID、姓名和期末考试成绩，要求每行能够对齐
    """
    m = sorted(class_sheet.items(),key =lambda item:item[1][1])
    print('%-5s  %-10s %-10s'%('ID','Name','Score'))
    for i in m:
        print('%-5d  %-10s %-10d'%(i[0],i[1][0],i[1][1]))

    # your code here....
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

