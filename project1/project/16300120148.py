#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

# __name__ = '__main__' 

""" 计算圆的面积
提示用户输入圆的半径求圆的面积，计算结果保留3位小数。
""" 

import math

def compute_circle_area(radius):
    area = math.pi * radius * radius 
    return area


def main():
    radius = input("请输入圆的半径 ==> ")  # '10.2'
    radius = float(radius)  # 10.2 
    area = compute_circle_area(radius)

    print()
    print('-' * 40)
    print()
    print("圆的面积 = %.3f" % area)
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
