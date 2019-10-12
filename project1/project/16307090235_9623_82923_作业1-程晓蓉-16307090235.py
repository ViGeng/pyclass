#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-


"""Project 1 直角三角形和其形成的锥形
提示输入直角三角形的底边和高，计算出直角三角形的周长面积，
以及旋转直角三角形形成锥形的表面积和体积，计算结果保留3位小数。
    perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
    area = (radius * height) / 2
    volume = math.pi * radius ** 2 * height / 3
    surface = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))

""" 


import math


def compute_cone_surface(radius, height):
    surface = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
    return surface

def compute_cone_volume(radius, height):
    volume = math.pi * radius ** 2 * height / 3
    return volume

def compute_right_triangle_perimeter(radius, height):
    perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
    return perimeter

def compute_right_triangle_area(radius, height):
    return (radius * height) / 2

def main():
    radius = input("请输入直角三角形的底边长度 => ")
    radius = float(radius)
    height = input("请输入直角三角形的高长度   => ")
    height = float(height)
    area = compute_right_triangle_area(radius, height)
    perimeter = compute_right_triangle_perimeter(radius, height)
    surface = compute_cone_surface(radius, height)
    volume = compute_cone_volume(radius, height) 


    print()
    print("----------------------------------------")
    print()
    print("%s%8.3f" %("直角三角形的底边长=", radius))
    print("%s%8.3f" %("  直角三角形的高长=", height))
    print("%s%8.3f" %("  直角三角形的面积=",area))
    print("%s%8.3f" %("  直角三角形的周长=",perimeter))
    print("%s%8.3f" %("      锥形的表面积=",surface))
    print("%s%8.3f" %("        锥形的体积=",volume))

   
if __name__ == '__main__':
    main()
