#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def e_value_default():
    '''e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ... + ...
    当某项小于默认极小值10**(-10)时结束
    '''
    e = 1    #初始结果（0!）
    i = 1  #i - 当前求和项数 item - 当前求和项
    denomi = 1   #denomi - 当前项分母（可阶乘）
    while 1/denomi >= 10**(-10):     #循环条件：当前求和项大于某极小值
        denomi *= i                  #分母阶乘
        e += 1/denomi                #当前结果
        i +=1

    return e,i


if __name__ == '__main__':
    e_default, loop_num = e_value_default()
    print('e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ... ≈ %s  *循环了%s次' % (e_default, loop_num))

    #用列表推导语句实现把几个项全部展开？
