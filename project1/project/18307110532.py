import math

def compute_right_triangle_perimeter(radius,height):
    perimeter=radius+height+(radius**2+height**2)**0.5
    return perimeter

def compute_right_triangle_area(radius,height):
    area=0.5*radius*height
    return area

def compute_cone_surface(radius,height):
    surface=math.pi*radius*(radius+(radius**2+height**2)**0.5)
    return surface

def compute_cone_volume(radius,height):
    volume=math.pi*radius**2/3
    return volume

def main():
    radius=input("请输入直角三角形的底边长度==>")
    radius = float(radius)
    height=input("请输入直角三角形的高长度==>")
    height = float(height)
    print('-' * 40)
    print()
    print("直角三角形的周长是 %.3f" % compute_right_triangle_perimeter(radius,height))
    print("直角三角形的面积是 %.3f"% compute_right_triangle_area(radius,height))
    print("锥形的表面积是%.3f"% compute_cone_surface(radius,height))
    print("锥形的体积是%.3f"% compute_cone_volume(radius,height))
    print()
    print('-' * 40)

if __name__ == '__main__':
    main()
