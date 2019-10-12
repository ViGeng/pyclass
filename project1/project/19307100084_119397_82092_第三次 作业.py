"""计算直角三角形的面积和周长 计算组
提示用户输入直角三角形的底边长和高长
"""
import math

def compute_right_triangle_perimeter(radius,height):
    perimeter = radius + height + ( radius**2 + height ** 2) ** 0.5
    return perimeter

def compute_right_triangle_area(radius,height):
    area= 0.5 * ( radius * height) 
    return area

def compute_cone_surface(radius,height):
    surface = math.pi * radius * ( radius + (radius**2 + height ** 2)**0.5)
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi * radius * radius+  height * 1/3
    return volume

def main():
    radius = input("请输入直角三角形的底边长度 ==> ")
    radius = float(radius)
    height = input("请输入直角三角形的高长度 ==> ")
    height = float(height)
    area=compute_right_triangle_area(radius,height)
    perimeter=compute_right_triangle_perimeter(radius,height)
    surface=compute_cone_surface(radius,height)
    volume=compute_cone_volume(radius,height)

    print()
    print('-' * 40)
    print()
    print("直角三角形的底边长= %10.3f" % radius)
    print("直角三角形的高长= %10.3f" % height)
    print("直角三角形的面积= %10.3f" % area)
    print("直角三角形的周长= %10.3f" % perimeter)
    print("锥形的表面积= %10.3f"% surface)
    print("锥形的体积= %10.3f"% volume)
    print('-' * 40)

if __name__=='__main__':
    main()
