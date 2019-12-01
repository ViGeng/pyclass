import project7_util as util

def get_class_sheet(total=25):
     class_sheet = dict()
     for i in range(total):         
          class_sheet[util.get_id()] = [util.get_name(),util.get_score()]    
          pass
     return class_sheet


def print_class_sheet(class_sheet):
    class_sheet_id = sorted(class_sheet)
    print('ID\tName\t\tScore')
    for i in range(len(class_sheet_id)):
        t = class_sheet_id[i]
        print('%3d\t%-8s\t%3d'%(t, class_sheet[t][0],class_sheet[t][1]))
    pass
     

def print_class_sheet_sorted(class_sheet):
    print('ID\tName\t\tScore')
    class_sheet_score=sorted(class_sheet.items(), key=lambda t:(t[1][1], t[1]))
    for i in range(len(class_sheet_score)):
        print('%3d\t%-8s\t%3d'%(class_sheet_score[i][0],class_sheet_score[i][1][0],class_sheet_score[i][1][1]))
    pass

def main():
    class_sheet = get_class_sheet()

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
