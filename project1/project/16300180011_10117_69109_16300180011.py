#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

# __name__ = '__main__' 

"""
Project 1 直角三角形和其形成的锥形 

提示用户输入底边和高
最后输出直角三角形的周长面积以及锥形的表面积和体积
计算结果保留 3 位小数

""" 

import math


def compute_right_triangle_perimeter(radius,height):
    perimeter = radius + height + math.sqrt(radius**2 + height**2)
    return perimeter

def compute_right_triangle_area(radius,height):
    area = 0.5 * radius * height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi * radius**2 * height/3
    return volume

def main():
    radius = input("请输入直角三角形的底边长度 ==> ")  # '5'
    radius = float(radius)  
    height = input("请输入直角三角形的高长度   ==> ")  # '8.5'
    height = float(height)  
    perimeter = compute_right_triangle_perimeter(radius,height)
    area = compute_right_triangle_area(radius,height)
    surface = compute_cone_surface(radius,height)
    volume = compute_cone_volume(radius,height)
    

    print()
    print('-' * 40)
    print()
    print('   直角三角形的底边长度 = ','%8.3f' % radius)
    print('       直角三角形的高长 = ','%8.3f' % height)
    print('       直角三角形的面积 = ','%8.3f' % area)
    print('       直角三角形的周长 = ','%8.3f' % perimeter)
    print('           锥形的表面积 = ','%8.3f' % surface)
    print('             锥形的体积 = ','%8.3f' % volume)
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
