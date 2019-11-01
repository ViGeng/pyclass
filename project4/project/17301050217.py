
got_number = int(input('请输入轮盘赌pocket的编号(0-36)==>'))
def judge():
    a = list(range(1,11,2))+list(range(19,29,2))+list(range(12,19,2))+list(range(20,37,2))
    b =list(range(2,11,2))+list(range(20,29,2))+list(range(11,19,2))+list(range(29,37,2))
    if got_number == 0:
        return 0
    elif got_number in a:
        return 1
    elif got_number in b:
        return 2
    else:
        return 3


def result_(item):
    colour = ['绿色','红色','黑色']
    if item == 3:
        print("编号不在[0,36]")
    elif item == 2:
        print('编号%d的颜色为%s' % (got_number,colour[item]))
    elif item == 1:
        print('编号%d的颜色为%s' % (got_number,colour[item]))
    elif item == 0:
        print('编号%d的颜色为%s' % (got_number,colour[item]))

if __name__=='__main__':
    a_judge = judge()
    result_(a_judge)
        
        
        
    
    
    
