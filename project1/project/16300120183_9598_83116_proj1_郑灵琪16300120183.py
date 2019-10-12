# -*- coding: utf-8 -*-
"""
直角三角形和其形成的锥形

"""

import math

def compute_right_triangle_perimeter(radius,height):
    perimeter = radius+height+math.sqrt(radius**2+height**2)
    return perimeter

def compute_right_triangle_area(radius,height):
    area = 0.5*radius*height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi*radius*(radius+math.sqrt(radius**2+height**2))
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi*(radius**2)*height/3
    return volume

def main():
    r = input("请输入直角三角形的底边长度 ==>")
    h = input("请输入直角三角形的高长度   ==>")
    r = float(r)
    h = float(h)
    print("直角三角形的底边长 = ", "%.3f" %r)
    print("直角三角形的高长 = ","%.3f" %h)
    print("直角三角形的面积 = ","%.3f" %compute_right_triangle_area(r,h))
    print("直角三角形的周长","%.3f" %compute_right_triangle_perimeter(r,h))
    print("锥形的表面积","%.3f" %compute_cone_surface(r,h))
    print("锥形的体积","%.3f" %compute_cone_volume(r,h))
    
if __name__ == "__main__":
    main()
