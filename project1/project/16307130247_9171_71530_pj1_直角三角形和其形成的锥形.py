#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

# __name__ = '__main__' 

""" 计算圆的面积
提示用户输入圆的半径求圆的面积，计算结果保留3位小数。
""" 

import math

def compute_right_triangle_perimeter(radius,height):
    return radius+height+math.sqrt(radius**2+height**2)

def compute_right_triangle_aera(radius,height):
    return 0.5*radius*height

def compute_cone_surface(radius,height):
    return math.pi*radius*(radius+math.sqrt(radius**2+height**2))

def compute_cone_volume(radius,height):
    return math.pi*radius**2*height/3
def main():
    radius = input("请输入三角形的底边长度 ==> ") 
    radius = float(radius)  # 10.2 
    height = input("请输入直角三角形的高长度 ==> ")
    height = float(height) 
    perimeter = compute_right_triangle_perimeter(radius, height)
    aera = compute_right_triangle_aera(radius,height)
    cone_surface = compute_cone_surface(radius,height)
    cone_volume = compute_cone_volume(radius,height)
    print()
    print('-' * 40)
    print()
    print("直角三角形的底边长 = %.3f" % radius)
    print("直角三角形的高长 = %.3f" % height)
    print("直角三角形的面积 = %.3f" % aera)
    print("直角三角形的周长 = %.3f" % perimeter)
    print("锥形的表面积 = %.3f" % cone_surface)
    print("锥形的体积 = %.3f" % cone_volume)
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
