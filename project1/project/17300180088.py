import math
def compute_right_triangle_perimeter(radius,height):
    right_triangle_perimeter = radius+height+(((radius**2)+(height**2))**0.5)
    return right_triangle_perimeter
def compute_right_triangle_area(radius,height):
    right_triangle_area = 0.5*radius*height
    return right_triangle_area
def compute_cone_surface(radius,height):
    cone_surface = math.pi*radius*(radius+((radius**2)+(height**2))**0.5)
    return cone_surface
def compute_cone_volume(radius,height):
    cone_volume = math.pi*(radius**2)*height/3
    return cone_volume
def main():
    radius=float(input('请输入圆锥底面园的半径：'))
    height=float(input('请输入圆锥的高度：'))
    right_triangle_perimeter = compute_right_triangle_perimeter(radius,height)
    right_triangle_area = compute_right_triangle_area(radius,height)
    cone_surface = compute_cone_surface(radius,height)
    cone_volume=compute_cone_volume(radius,height)
    print('直角三角形周长为:%.3f' %right_triangle_perimeter)
    print('直角三角形面积为:%.3f' %right_triangle_area)
    print('锥形表面积为:%.3f' %cone_surface)
    print('锥形面积为:%.3f' %cone_volume )
if __name__ == '__main__':
    main()