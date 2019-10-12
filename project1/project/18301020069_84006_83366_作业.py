import math

def compute_right_triangle_area(radius,height):
    area = 1 / 2 * radius * height
    return area

def compute_right_triangle_perimeter(radius,height):
    circumference = radius + height + math.sqrt(radius ** 2 + height ** 2)
    return circumference

def compute_cone_surface(radius,height):
    surface = math.pi * radius * radius + math.sqrt(radius ** 2 + height ** 2) * math.pi * radius
    return surface

def compute_cone_volume(radius,height):
    volume=math.pi*radius*radius*height
    return  volume


def main():
    radius=input("请输入直角三角形的底边长度==>")
    height=input("请输入直角三角形的高长度==>")
    radius=float(radius)
    height=float(height)
    area= compute_right_triangle_area(radius,height)
    circumference=compute_right_triangle_perimeter(radius,height)
    surface=compute_cone_surface(radius,height)
    volume=compute_cone_volume(radius,height)

    print("直角三角形的底边长=",radius)
    print("直角三角形的高长=",height)
    print("直角三角形的面积=",area)
    print("直角三角形的周长=",circumference)
    print("锥形的表面积=",surface)
    print("锥形的体积=",volume)

if __name__=="__main__":
    main()