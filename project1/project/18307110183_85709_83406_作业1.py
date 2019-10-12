#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# __name__ = '__main__'

"""计算直角三角形的周长、面积；计算锥形的表面积、体积；
结果均保留三位小数"""

import math

def compute_right_triangle_primeter(radius,height):
    primeter = radius + height + (radius ** 2 + height ** 2) ** 0.5
    return primeter

def compute_right_triangle_area(radius,height):
    area = 0.5 * radius * height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi * radius * (radius +
    (radius ** 2 + height ** 2) ** 0.5)
    return surface

def compute_cone_volume(radius,height):
    volume = (1/3) * math.pi * radius ** 2 * height
    return volume

def main():
    radius = float(input("请输入三角形的底边："))
    height = float(input("请输入三角形的高："))
    primeter = compute_right_triangle_primeter(radius,height)
    area = compute_right_triangle_area(radius,height)
    surface = compute_cone_surface(radius,height)
    volume = compute_cone_volume(radius,height)

    print()
    print("直角三角形的底边长 = %.3f" % radius)
    print("直角三角形的高 = %.3f" % height)
    print()
    print('-' * 30)
    print()
    print("直角三角形的周长 = %.3f" % primeter)
    print("直角三角形的面积 = %.3f" % area)
    print("锥形的表面积 = %.3f" % surface)
    print("锥形的体积 = %.3f" % volume)

if __name__ == '__main__':
    main()
    
                   
