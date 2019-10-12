import math

def compute_right_triangle_perimeter(radius, height):
    distance = radius ** 2 + height ** 2
    distance = math.sqrt(distance)
    perimeter = distance + radius + height
    return perimeter

def compute_right_triangle_area(radius, height):
    area = radius * height / 2
    return area

def compute_cone_surface(radius, height):
    distance = radius ** 2 + height ** 2
    distance = math.sqrt(distance)
    surface = math.pi * radius * (radius + distance)
    return surface

def compute_cone_volume(radius, height):
    volumn = math.pi * radius * radius * height / 3
    return volumn

def main():
    radius = input('请输入直角三角形的底边长度 ==>')
    radius = float(radius)
    height = input('请输入直角三角形的高长度   ==>')
    height = float(height)
    perimeter = compute_right_triangle_perimeter(radius, height)
    area = compute_right_triangle_area(radius, height)
    surface = compute_cone_surface(radius, height)
    volumn = compute_cone_volume(radius, height)

    print()
    print('-' * 40)
    print()
    print('直角三角形的底边长 = %.3f' % radius)
    print('  直角三角形的高长 = %.3f' % height)
    print('  直角三角形的面积 = %.3f' % area)
    print('    直角三角形周长 = %.3f' % perimeter)
    print('      锥体的表面积 = %.3f' % surface)
    print('        锥体的体积 = %.3f' % volumn)
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
    
