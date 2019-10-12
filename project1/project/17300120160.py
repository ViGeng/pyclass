""" 计算直角三角形和其形成的锥形
输入直角三角形的底边和高，
计算结果保留3位小数。""" 

import math


def compute_right_triangle_perimeter(height, radius):
    perimeter = height+radius+(radius*radius+height*height)**0.5
    return perimeter
def compute_right_triangle_area(height, radius):
    area = radius*height 
    return area
def compute_cone_surface(height, radius):
    surface = math.pi * radius * (radius+(radius*radius+height*height)**0.5)
    return surface
def compute_cone_volume(height, radius):
    volume = math.pi * radius * height/3 
    return volume

def main():
    height = input("请输入高 ==> ")
    radius = input("请输入底边==>")
    radius = float(radius)  
    height = float(height)

    perimeter = compute_right_triangle_perimeter(height, radius)
    area = compute_right_triangle_perimeter(height, radius)
    surface=compute_cone_surface(height, radius)
    volume=compute_cone_volume(height, radius)

    print()
    print('-' * 40)
    print()
    print("直角三角形周长 = %.3f" % perimeter)
    print("直角三角形面积 = %.3f" % area)
    print("锥形表面积 = %.3f" % surface)
    print("锥形体积 = %.3f" % volume)
    print()
    print('-' * 40)
if __name__ == '__main__':
    main()

