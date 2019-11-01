
pocket = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
colour = ['绿色','黑色', '红色']

def give_colour1():
    if pocket % 2 == 0:
        return 1 #黑色
    else:
        return 2 #红色

def give_colour2():
    if pocket % 2 == 0:
        return 2 #红色
    else:
        return 1 #黑色
    
def get_colour1(pocket):
    if pocket <0 or pocket >36:
        print('编号不在[0, 36]')
    else:
        def get_colour2(pocket):
            if pocket == 0:
                return 0
            elif pocket >= 1 and pocket < 11:
                return give_colour1()
            elif pocket >= 11 and pocket < 19:
                return give_colour2()
            elif pocket >= 19 and pocket < 29:
                return give_colour1()
            elif pocket >= 29 and pocket <= 36:
                return give_colour2()
        p_colour = get_colour2(pocket)
        print('编号为%s的pocket颜色为%s'%(pocket,colour[p_colour]))

if __name__ == '__main__':
   get_colour1(pocket)
    

    
        
    

