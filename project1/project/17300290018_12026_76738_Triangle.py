#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

# __name__ = '__main__'

"""在已知一个直角三角形的底边 radius 和高 height 的情况下，可以计算出直角三角形的
周长和面积。通过旋转直角三角形，可以形成一个锥形，计算锥形的表面积和体积。
"""

from math import sqrt
from math import pi

def compute_right_triangle_perimeter(radius, height):
    Perimeter = radius + height + sqrt(radius ** 2 + height ** 2)
    return Perimeter

def compute_right_triangle_area(radius, height):
    Area = radius * height / 2
    return Area

def compute_cone_surface(radius, height):
    Surface = pi * radius * (radius + sqrt(radius ** 2 + height ** 2))
    return Surface

def compute_cone_volume(radius, height):
    Volume = pi * radius ** 2 * height / 3
    return Volume

def main():
    Radius = float(input("请输入直角三角形的底边长度 ==> "))
    Height = float(input("请输入直角三角形的高长度   ==> "))
    
    print("------------------------------------------")
    print("%s = %10.3f" %("直角三角形的底边长", Radius))
    print("%s = %10.3f" %("  直角三角形的高长", Height))
    print("%s = %10.3f" %("  直角三角形的面积", compute_right_triangle_area(Radius, Height)))
    print("%s = %10.3f" %("  直角三角形的周长", compute_right_triangle_perimeter(Radius, Height)))
    print("%s = %10.3f" %("      锥形的表面积", compute_cone_surface(Radius, Height)))
    print("%s = %10.3f" %("      锥形的表面积", compute_cone_volume(Radius, Height)))
    print("------------------------------------------")

if __name__ == '__main__':
    main()


    
