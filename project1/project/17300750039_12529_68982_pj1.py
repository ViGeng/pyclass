""" 提示用户输入底边和高，按照公式计算出结果，最后输出：
直角三角形的周长面积以及锥形的表面积和体积，计算结果保留 3 位小数。
"""

import math

def computer_right_triangle_perimeter(radius,height):
    perimeter = radius + height + math.sqrt(radius**2 + height**2)
    return perimeter

def computer_right_triangle_area(radius,height):
    area = 0.5 * radius * height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi * radius**2 * height/3
    return volume

def main():
    radius = input("请输入直角三角形的底边长度 ==> ")
    height = input("请输入直角三角形的高长度   ==> ")
    radius = float(radius)
    height = float(height)

    perimeter = computer_right_triangle_perimeter(radius,height)
    area = computer_right_triangle_area(radius,height)
    surface = compute_cone_surface(radius,height)
    volume = compute_cone_volume(radius,height)

    print()
    print('-' * 40)
    print()
    print("直角三角形的底边长 = %8.3f" % radius)
    print("  直角三角形的高长 = %8.3f" % height)
    print("  直角三角形的面积 = %8.3f" % area)
    print("  直角三角形的周长 = %8.3f" % perimeter)
    print("      锥形的表面积 = %8.3f" % surface)
    print("        锥形的体积 = %8.3f" % volume)
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
