import math

def compute_right_triangle_perimeter(radius,height):
    perimeter = radius + height + math.sqrt(radius * radius + height * height)
    return perimeter

def compute_right_triangle_area(radius,height):
    area = 0.5 * radius * height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi * radius * (radius + math.sqrt(radius * radius + height * height))
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi * radius * radius * height / 3
    return volume

def main():
    radius = input("请输入直角三角形的底边长度 ==> ")
    radius = float(radius)
    height = input("请输入直角三角形的高长度   ==> ")
    height = float(height)
    area = compute_right_triangle_area(radius,height)
    perimeter = compute_right_triangle_perimeter(radius,height)
    surface = compute_cone_surface(radius,height)
    volume = compute_cone_volume(radius,height)
    print()
    print("-" * 40)
    print()
    print("%14s %2s %8.3f" % ("直角三角形的底边长","=",radius))
    print("%15s %2s %8.3f" % ("直角三角形的高长","=",height))
    print("%15s %2s %8.3f" % ("直角三角形的面积","=",area))
    print("%15s %2s %8.3f" % ("直角三角形的周长","=",perimeter))
    print("%17s %2s %8.3f" % ("锥形的表面积","=",surface))
    print("%18s %2s %8.3f" % ("锥形的体积","=",volume))

    print()
    print("-" * 40)

if __name__ == "__main__":
    main()
