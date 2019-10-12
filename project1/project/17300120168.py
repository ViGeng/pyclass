import math

def compute_right_triangle_perimeter(radius, height):
    perimeter = radius + height + math.sqrt(radius * radius + height * height)
    return perimeter

def compute_right_triangle_area(radius, height):
    area = (1/2) * radius * height
    return area


def compute_cone_surface(radius, height):
    t = math.sqrt(radius * radius + height * height)
    surface = math.pi * radius * (radius + t)
    return surface


def compute_cone_volume(radius, height):
    volume = (1/3) * math.pi * radius * radius * height
    return volume

def main():
    radius = input("请输入直角三角形的底边长度 ==> ")
    radius = float(radius)
    height = input("请输入直角三角形的高长度 ==> ")
    height = float(height)
    perimeter = compute_right_triangle_perimeter(radius, height)
    area = compute_right_triangle_area(radius, height)
    surface = compute_cone_surface(radius, height)
    volume = compute_cone_volume(radius, height)

    print()
    print('-' * 40)
    print()
    print("直角三角形的底边长 = %.3f"%radius)
    print("直角三角形的高长 = %.3f" % height)
    print("直角三角形的面积 = %.3f" % area)
    print("直角三角形的周长 = %.3f" % perimeter)
    print("锥形的表面积 = %.3f" % surface)
    print("锥形的体积 = %.3f" % volume)
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
    
