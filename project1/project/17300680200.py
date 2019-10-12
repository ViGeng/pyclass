import math

def compute_right_triangle_perimeter(height,radius):
    perimeter = radius + height + math.sqrt(radius**2 + height**2)
    return perimeter

def compute_right_triangle_area(height,radius):
    area = (1/2) * radius * height
    return area

def compute_right_triangle_surface(height,radius):
    surface = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    return surface

def compute_right_triangle_volume(height,radius):
    volume = math.pi * radius**2 * (height/3)
    return volume

def main():
    radius = input("请输入直角三角形的底边长度 ==>") # 5
    radius = float(radius)
    height = input("请输入直角三角形的高长度   ==>")
    height = float(height)
    perimeter = compute_right_triangle_perimeter(height,radius)
    area = compute_right_triangle_area(height,radius)
    surface = compute_right_triangle_surface(height,radius)
    volume = compute_right_triangle_volume(height,radius)

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
    
