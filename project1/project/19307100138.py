#__name__ = '__main__'
"""面积和锥形的表面积、体积
提示用户输入直角三角形的底边长度和高长度，求直角三角形的周长、面积和锥形的表面积、体积，计算结果保留3位小数。
"""

import math

def compute_right_triangle_perimeter(radius,height):
    perimeter=radius+height+(radius*radius+height*height)**0.5
    return perimeter
def compute_right_triangle_area(radius,height):
    area=0.5*radius*height
    return area
def compute_cone_surface(radius,height):
    surface=math.pi*radius*(radius+(radius*radius+height*height)**0.5)
    return surface
def compute_cone_volume(radius,height):
    volume=math.pi*radius*radius*height/3
    return volume

def main():
    radius=input("请输入直角三角形的底边长度==>") # '10.3'
    radius=float(radius) # 10.3
    height=input("  请输入直角三角形的高长度==>") # '10.3'
    height=float(height) # 10.3
    perimeter=compute_right_triangle_perimeter(radius,height)
    area=compute_right_triangle_area(radius,height)
    surface=compute_cone_surface(radius,height)
    volume=compute_cone_volume(radius,height)
    print()
    print('-'*40)
    print()
    print("直角三角形的底边长=%.3f" % radius)
    print("  直角三角形的高长=%.3f" % height)
    print("  直角三角形的周长=%.3f" % perimeter)
    print("  直角三角形的面积=%.3f" % area)
    print("      锥形的表面积=%.3f" % surface)
    print("        锥形的体积=%.3f" % volume)
    print()
    print('-'*40)

if __name__ == '__main__':
    main()
