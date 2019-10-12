
"""计算直角三角形的周长和面积、锥形的表面积和体积
提示用户输入底边和高，按照公式计算出结果，计算结果保留3位小数。
"""

import math

def compute_right_triangle_perometer(radius,height):
    perometer = radius + height + math.sqrt(radius ** 2 + height ** 2)
    return perometer

def compute_right_triangle_area(radius,height):
    area = 1/2 * radius * height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi * radius * radius * height/3
    return volume


def main():
    radius = input("请输入直角三角形的底边 ==> ")
    height = input("请输入直角三角形的高   ==> ")
    radius = float(radius)
    height = float(height)
    perometer = compute_right_triangle_perometer(radius,height)
    area = compute_right_triangle_area(radius,height)
    surface = compute_cone_surface(radius,height)
    volume = compute_cone_volume(radius,height)


    print()
    print('-' * 40)
    print()
    print("%20s = %6.3f" % ("直角三角形的周长",perometer))
    print("%20s = %6.3f" % ("直角三角形的周长",area))
    print("%22s = %6.3f" % ("锥形的表面积",surface))
    print("%23s = %6.3f" % ("锥形的体积",volume))
    print()
    print('-' * 40)


if __name__ == '__main__':
    main()





    
