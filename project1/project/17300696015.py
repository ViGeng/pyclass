import math

def compute_right_triangle_perimeter (radius,height):
    Perimeter = radius + height + (radius**2 + height**2)**0.5
    return round (Perimeter,3)

def compute_right_triangle_area (radius,height):
    Area = 1/2 * radius * height
    return round (Area,3)

def compute_cone_surface (radius,height):
    Surface = math.pi * radius * (radius + (radius**2 + height**2)**0.5)
    return round (Surface,3)

def compute_cone_volume (radius,height):
    Volume = math.pi * radius**2 * height/3
    return round (Volume,3)


def main():
    radius = input('请输入直角三角形的底边长度 ==> ')  
    height = input('请输入直角三角形的高长度 ==> ')
    radius = float(radius)
    height = float(height)
    Perimeter = compute_right_triangle_perimeter (radius,height)
    Area = compute_right_triangle_area (radius,height)
    Surface = compute_cone_surface (radius,height)
    Volume = compute_cone_volume (radius,height)

    print('直角三角形的底边长 = %.3f' % radius)
    print('直角三角形的高长 = %.3f' % height)
    print('直角三角形的面积 = %.3f' % Area)
    print('直角三角形的周长 = %.3f' % Perimeter)
    print('锥形的表面积 = %.3f' % Surface)
    print('锥形的体积 = %.3f' % Volume)
 
if __name__ == '__main__':
    main()


